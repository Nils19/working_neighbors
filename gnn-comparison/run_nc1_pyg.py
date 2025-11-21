#!/usr/bin/env python
import argparse, random, numpy as np, torch, torch.nn.functional as F
from torch import nn
from torch_geometric.datasets import TUDataset
from torch_geometric.transforms import NormalizeFeatures
from torch_geometric.loader import DataLoader
from torch_geometric.nn import GCNConv, GINConv, GATConv, SAGEConv, BatchNorm, global_mean_pool
from sklearn.model_selection import StratifiedKFold, train_test_split

def set_seed(s=42):
    random.seed(s); np.random.seed(s); torch.manual_seed(s); torch.cuda.manual_seed_all(s)

def dev():
    return torch.device("mps" if torch.backends.mps.is_available() else "cpu")

class GCN(nn.Module):
    def __init__(self, in_dim, hidden, out_dim, layers=3, drop=0.5):
        super().__init__()
        self.convs=nn.ModuleList(); self.bns=nn.ModuleList()
        dims=[in_dim]+[hidden]*(layers-1)
        for d in dims:
            self.convs.append(GCNConv(d, hidden)); self.bns.append(BatchNorm(hidden))
        self.drop=drop
        self.head=nn.Sequential(nn.Linear(hidden,hidden), nn.ReLU(), nn.Dropout(drop), nn.Linear(hidden,out_dim))
    def forward(self,x,ei,b):
        for conv,bn in zip(self.convs,self.bns):
            x=conv(x,ei); x=bn(x); x=F.relu(x); x=F.dropout(x,p=self.drop,training=self.training)
        return self.head(global_mean_pool(x,b))

class GIN(nn.Module):
    def __init__(self, in_dim, hidden, out_dim, layers=5, drop=0.5):
        super().__init__()
        self.layers=nn.ModuleList(); self.bns=nn.ModuleList()
        def mlp(din, dout): return nn.Sequential(nn.Linear(din, hidden), nn.ReLU(), nn.Linear(hidden, dout))
        self.layers.append(GINConv(mlp(in_dim, hidden)))
        self.bns.append(BatchNorm(hidden))
        for _ in range(layers-1):
            self.layers.append(GINConv(mlp(hidden, hidden))); self.bns.append(BatchNorm(hidden))
        self.drop=drop
        self.head=nn.Sequential(nn.Linear(hidden, hidden), nn.ReLU(), nn.Dropout(drop), nn.Linear(hidden, out_dim))
    def forward(self,x,ei,b):
        for conv,bn in zip(self.layers,self.bns):
            x=conv(x,ei); x=bn(x); x=F.relu(x); x=F.dropout(x,p=self.drop,training=self.training)
        return self.head(global_mean_pool(x,b))

class GAT(nn.Module):
    def __init__(self, in_dim, hidden, out_dim, layers=3, heads=4, drop=0.5):
        super().__init__()
        self.layers=nn.ModuleList(); self.bns=nn.ModuleList()
        self.layers.append(GATConv(in_dim, hidden//heads, heads=heads, concat=True)); self.bns.append(BatchNorm(hidden))
        for _ in range(layers-1):
            self.layers.append(GATConv(hidden, hidden//heads, heads=heads, concat=True)); self.bns.append(BatchNorm(hidden))
        self.drop=drop
        self.head=nn.Sequential(nn.Linear(hidden,hidden), nn.ReLU(), nn.Dropout(drop), nn.Linear(hidden,out_dim))
    def forward(self,x,ei,b):
        for conv,bn in zip(self.layers,self.bns):
            x=conv(x,ei); x=bn(x); x=F.elu(x); x=F.dropout(x,p=self.drop,training=self.training)
        return self.head(global_mean_pool(x,b))

class GraphSAGE(nn.Module):
    def __init__(self, in_dim, hidden, out_dim, layers=3, drop=0.5):
        super().__init__()
        self.convs=nn.ModuleList([SAGEConv(in_dim, hidden)]+[SAGEConv(hidden, hidden) for _ in range(layers-1)])
        self.bns=nn.ModuleList([BatchNorm(hidden) for _ in range(layers)])
        self.drop=drop
        self.head=nn.Sequential(nn.Linear(hidden,hidden), nn.ReLU(), nn.Dropout(drop), nn.Linear(hidden,out_dim))
    def forward(self,x,ei,b):
        for conv,bn in zip(self.convs,self.bns):
            x=conv(x,ei); x=bn(x); x=F.relu(x); x=F.dropout(x,p=self.drop,training=self.training)
        return self.head(global_mean_pool(x,b))

def step(model, loader, device, opt=None):
    train = opt is not None
    if train: model.train()
    else: model.eval()
    tot=correct=0; loss_sum=0.0
    with torch.set_grad_enabled(train):
        for batch in loader:
            batch = batch.to(device)
            out = model(batch.x, batch.edge_index, batch.batch)
            loss = F.cross_entropy(out, batch.y)
            if train: opt.zero_grad(); loss.backward(); opt.step()
            loss_sum += float(loss)*batch.num_graphs
            pred = out.argmax(-1)
            correct += int((pred==batch.y).sum())
            tot += batch.num_graphs
    return loss_sum/max(1,tot), correct/max(1,tot)

def run_single_split(ds, model_name="gin", hidden=64, layers=5, epochs=200, bs=128, lr=1e-3, wd=5e-4, seed=42, device=torch.device("cpu")):
    # 80/10/10 stratified split
    y = np.array([int(d.y) for d in ds])
    idx = np.arange(len(ds))
    tr, tmp, y_tr, y_tmp = train_test_split(idx, y, test_size=0.2, stratify=y, random_state=seed)
    va, te = train_test_split(tmp, test_size=0.5, stratify=y_tmp, random_state=seed)
    tr_loader = DataLoader(ds[tr], batch_size=bs, shuffle=True)
    va_loader = DataLoader(ds[va], batch_size=bs)
    te_loader = DataLoader(ds[te], batch_size=bs)

    in_dim, out_dim = ds.num_features, ds.num_classes
    model = {"gcn":GCN, "gin":GIN, "gat":GAT, "sage":GraphSAGE}[model_name](in_dim, hidden, out_dim, layers=layers).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=wd)

    best_val=0.0; best_test=0.0
    for ep in range(1, epochs+1):
        tr_loss,tr_acc = step(model,tr_loader,device,opt)
        va_loss,va_acc = step(model,va_loader,device)
        te_loss,te_acc = step(model,te_loader,device)
        if va_acc>best_val: best_val, best_test = va_acc, te_acc
        if ep%10==0 or ep==1:
            print(f"Ep {ep:03d} | train {tr_acc:.3f} | val {va_acc:.3f} | test {te_acc:.3f} | best(val)->test {best_test:.3f}")
    return best_test

def run_kfold(ds, folds=10, **h):
    y = np.array([int(d.y) for d in ds])
    skf = StratifiedKFold(n_splits=folds, shuffle=True, random_state=h.get("seed",42))
    accs=[]
    for k,(tr_idx,te_idx) in enumerate(skf.split(np.zeros(len(y)), y), 1):
        # hold out a small val set from train (10%)
        y_tr = y[tr_idx]
        tr_sub, va_sub = train_test_split(tr_idx, test_size=0.1, stratify=y_tr, random_state=h.get("seed",42))
        tr_loader = DataLoader(ds[tr_sub], batch_size=h["bs"], shuffle=True)
        va_loader = DataLoader(ds[va_sub], batch_size=h["bs"])
        te_loader = DataLoader(ds[te_idx], batch_size=h["bs"])
        in_dim, out_dim = ds.num_features, ds.num_classes
        model = {"gcn":GCN, "gin":GIN, "gat":GAT, "sage":GraphSAGE}[h["model"]](in_dim, h["hidden"], out_dim, layers=h["layers"]).to(h["device"])
        opt = torch.optim.Adam(model.parameters(), lr=h["lr"], weight_decay=h["wd"])
        best_val=0.0; best_test=0.0
        for ep in range(1, h["epochs"]+1):
            step(model,tr_loader,h["device"],opt)
            va_loss,va_acc = step(model,va_loader,h["device"])
            te_loss,te_acc = step(model,te_loader,h["device"])
            if va_acc>best_val: best_val, best_test = va_acc, te_acc
        accs.append(best_test); print(f"Fold {k}/{folds} best test: {best_test:.4f}")
    print(f"{folds}-fold mean±std: {np.mean(accs):.4f} ± {np.std(accs):.4f}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["gin","gcn","gat","sage"], default="gin")
    ap.add_argument("--hidden", type=int, default=64)
    ap.add_argument("--layers", type=int, default=5)          # GIN likes deeper
    ap.add_argument("--epochs", type=int, default=200)
    ap.add_argument("--batch_size", type=int, default=128)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--wd", type=float, default=5e-4)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--kfold", type=int, default=0, help="0 for 80/10/10 split; otherwise K for K-fold CV")
    args = ap.parse_args()

    set_seed(args.seed); device = dev()
    ds = TUDataset(root="./data", name="NCI1", use_node_attr=True, transform=NormalizeFeatures())
    if args.kfold and args.kfold > 1:
        run_kfold(ds, folds=args.kfold, model=args.model, hidden=args.hidden, layers=args.layers,
                  epochs=args.epochs, bs=args.batch_size, lr=args.lr, wd=args.wd, seed=args.seed, device=device)
    else:
        acc = run_single_split(ds, model_name=args.model, hidden=args.hidden, layers=args.layers,
                               epochs=args.epochs, bs=args.batch_size, lr=args.lr, wd=args.wd,
                               seed=args.seed, device=device)
        print(f"Single-split best test acc: {acc:.4f}")

if __name__ == "__main__":
    main()
