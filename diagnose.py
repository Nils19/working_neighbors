#!/usr/bin/env python
"""
Diagnostic script to check what's wrong with training.
"""
import torch
import main
from common import Task, STOP, GNN_TYPE
from experiment import Experiment

print("="*60)
print("DIAGNOSTIC CHECK")
print("="*60)

# Check PyTorch and device
print(f"\n1. PyTorch version: {torch.__version__}")
print(f"   CUDA available: {torch.cuda.is_available()}")
print(f"   MPS available: {torch.backends.mps.is_available()}")
print(f"   MPS built: {torch.backends.mps.is_built()}")

if torch.cuda.is_available():
    device = torch.device('cuda')
elif torch.backends.mps.is_available():
    device = torch.device('mps')
else:
    device = torch.device('cpu')
print(f"   Selected device: {device}")

# Check dataset generation
print("\n2. Dataset generation check:")
task = Task.NEIGHBORS_MATCH
depth = 4
from tasks.dictionary_lookup import DictionaryLookupDataset
dataset = DictionaryLookupDataset(depth)
X_train, X_test, dim0, out_dim, criterion = dataset.generate_data(0.8)
print(f"   Depth: {depth}")
print(f"   Training samples: {len(X_train)}")
print(f"   Test samples: {len(X_test)}")
print(f"   Input dim: {dim0}")
print(f"   Output dim: {out_dim}")
print(f"   First train sample label: {X_train[0].y}")
print(f"   Label distribution: {[sum([1 for d in X_train if d.y == i]) for i in range(out_dim)]}")

# Check model initialization
print("\n3. Model check:")
args = main.get_fake_args(
    task=Task.NEIGHBORS_MATCH,
    depth=4,
    num_layers=5,
    batch_size=1024,
    type=GNN_TYPE.GAT,
    stop=STOP.TRAIN,
)
exp = Experiment(args)
print(f"   Model device: {exp.device}")
print(f"   Batch size: {exp.batch_size}")
print(f"   Num layers: {exp.num_layers}")
print(f"   GNN type: {exp.type}")
print(f"   Model parameters: {sum(p.numel() for p in exp.model.parameters()):,}")

# Quick forward pass test
print("\n4. Forward pass test:")
test_batch = X_train[0].to(exp.device)
with torch.no_grad():
    output = exp.model(test_batch)
    print(f"   Output shape: {output.shape}")
    print(f"   Output (first 5 values): {output[0, :5].cpu().numpy()}")
    
# Test one training step
print("\n5. Single training step test:")
from torch_geometric.loader import DataLoader
loader = DataLoader([X_train[0]] * 32, batch_size=32, shuffle=False)
batch = next(iter(loader)).to(exp.device)
exp.optimizer.zero_grad()
output = exp.model(batch)
loss = exp.criterion(output, batch.y)
loss.backward()
exp.optimizer.step()
print(f"   Loss: {loss.item():.4f}")
print(f"   Loss is finite: {torch.isfinite(loss).item()}")
print(f"   Gradients exist: {any(p.grad is not None for p in exp.model.parameters())}")
grad_norm = sum(p.grad.norm().item() for p in exp.model.parameters() if p.grad is not None)
print(f"   Total gradient norm: {grad_norm:.4f}")

print("\n" + "="*60)
print("DIAGNOSIS COMPLETE")
print("="*60)
print("\nIf you see any issues above (NaN, wrong device, etc), that's the problem!")
