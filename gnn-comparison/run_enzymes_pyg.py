# minimal ENZYMES trainer (GCN/GAT) — works with current PyG
import argparse, random, numpy as np, torch, torch.nn.functional as F
from torch import nn
from torch_geometric.datasets import TUDataset
from torch_geometric.transforms import NormalizeFeatures
from torch_geometric.loader import DataLoader
from torch_geometric.nn import GCNConv, GATConv, BatchNorm, global_mean_pool

def set_seed(s): random.seed(s); np.random.seed(s); torch.manual_seed(s); torch.cuda.manual_seed_all(s)
def dev(): return torch.device("mps" if torch.backends.mps.is_available() else "cpu")

class GCN(nn.Module):
    def __init__(self, in_dim, hidden, out_dim, layers=3, drop=0.5):
        super().__init__()
        self.convs, self.bns = nn.ModuleList(), nn.ModuleList()
        dims = [in_dim] + [hidden]*(layers-1)
        for d_in in dims:
            self.convs.append(GCNConv(d_in, hidden)); self.bns.append(BatchNorm(hidden))
        self.drop = drop; self.head = nn.Sequential(nn.Linear(hidden, hidden), nn.ReLU(), nn.Dropout(drop), nn.Linear(hidden, out_dim))
    def forward(self, x, ei, b):
        for conv,bn in zip(self.convs,self.bns):
            x = F.dropout(F.relu(bn(conv(x,ei))), p=self.drop, training=self.training)
        return self.head(global_mean_pool(x,b))

class GAT(nn.Module):
    def __init__(self, in_dim, hidden, out_dim, layers=3, heads=4, drop=0.5):
        super().__init__()
        self.layers, self.bns = nn.ModuleList(), nn.ModuleList()
        self.layers.append(GATConv(in_dim, hidden//heads, heads=heads, concat=True)); self.bns.append(BatchNorm(hidden))
        for _ in range(layers-1):
            self.layers.append(GATConv(hidden, hidden//heads, heads=heads, concat=True)); self.bns.append(BatchNorm(hidden))
        self.drop = drop; self.head = nn.Sequential(nn.Linear(hidden, hidden), nn.ReLU(), nn.Dropout(drop), nn.Linear(hidden, out_dim))
    def forward(self, x, ei, b):
        for conv,bn in zip(self.layers,self.bns):
            x = F.dropout(F.elu(bn(conv(x,ei))), p=self.drop, training=self.training)
        return self.head(global_mean_pool(x,b))

def split_idxs(y, seed=42):
    from sklearn.model_selection import train_test_split
    idx = np.arange(len(y))
    tr, tmp, y_tr, y_tmp = train_test_split(idx, y, test_size=0.2, stratify=y, random_state=seed)
    va, te = train_test_split(tmp, test_size=0.5, stratify=y_tmp, random_state=seed)
    return tr, va, te

def run(model_name="gcn", hidden=64, layers=3, epochs=200, bs=64, lr=1e-3, wd=5e-4, seed=42):
    set_seed(seed); device = dev()
    ds = TUDataset(root="./data", name="ENZYMES", use_node_attr=True, transform=NormalizeFeatures())
    y = np.array([int(d.y) for d in ds]); tr, va, te = split_idxs(y, seed)
    tr_loader = DataLoader(ds[tr], batch_size=bs, shuffle=True); va_loader = DataLoader(ds[va], batch_size=bs); te_loader = DataLoader(ds[te], batch_size=bs)
    in_dim, out_dim = ds.num_features, ds.num_classes
    model = (GCN if model_name=="gcn" else GAT)(in_dim, hidden, out_dim, layers=layers).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=wd)

    def epoch(loader, train):
        if train: model.train()
        else: model.eval()
        tot_loss=tot=correct=0
        with torch.set_grad_enabled(train):
            for b in loader:
                b=b.to(device); out=model(b.x,b.edge_index,b.batch); loss=F.cross_entropy(out,b.y)
                if train: opt.zero_grad(); loss.backward(); opt.step()
                tot_loss += float(loss)*b.num_graphs; pred=out.argmax(-1); correct += int((pred==b.y).sum()); tot += b.num_graphs
        return tot_loss/tot, correct/tot

    best_val=best_test=0.0
    for e in range(1, epochs+1):
        tr_loss,tr_acc = epoch(tr_loader, True)
        va_loss,va_acc = epoch(va_loader, False)
        te_loss,te_acc = epoch(te_loader, False)
        if va_acc>best_val: best_val, best_test = va_acc, te_acc
        if e%10==0 or e==1: print(f"Ep {e:03d} | train {tr_acc:.3f} | val {va_acc:.3f} | test {te_acc:.3f} | best(val)->test {best_test:.3f}")
    print(f"Best test (by val): {best_test:.4f}")

if __name__=="__main__":
    import argparse; p=argparse.ArgumentParser()
    p.add_argument("--model", choices=["gcn","gat"], default="gcn")
    p.add_argument("--hidden", type=int, default=64)
    p.add_argument("--layers", type=int, default=3)
    p.add_argument("--epochs", type=int, default=200)
    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--wd", type=float, default=5e-4)
    p.add_argument("--seed", type=int, default=42)
    a=p.parse_args(); run(a.model,a.hidden,a.layers,a.epochs,a.batch_size,a.lr,a.wd,a.seed)
