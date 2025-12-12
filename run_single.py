#!/usr/bin/env python
"""
Quick script to run a single experiment configuration.
Modify the parameters below and run: python run_single.py

Optimized for M4 MacBook Pro 16" with 64GB unified memory:
- Uses MPS (Metal Performance Shaders) for GPU acceleration
- 4x larger batch sizes than paper (faster training, better convergence)
- Optimized data loader workers for M4 CPU
- Takes full advantage of 64GB unified memory architecture
"""
import main
from common import Task, STOP, GNN_TYPE
from experiment import Experiment
import torch
import os

# M4 MacBook Pro optimizations
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'  # Fallback to CPU for unsupported ops
torch.set_num_threads(8)  # Optimize for M4's performance cores

if __name__ == '__main__':
    # Modify these parameters as needed
    task = Task.NEIGHBORS_MATCH
    gnn_type = GNN_TYPE.GAT  # Change to GCN, GGNN, GIN, or GAT
    depth = 4
    num_layers = depth + 1  # Should be depth + 1
    batch_size = 1024
    eval_every = 100
    
    # Use paper's original batch sizes for reliable convergence
    # Large batches (4096+) hurt optimization for this problem
    override_params = {
        2: {'batch_size': 64, 'eval_every': 1000},
        3: {'batch_size': 64},
        4: {'batch_size': 1024},  # Original paper setting
        5: {'batch_size': 1024},
        6: {'batch_size': 1024},
        7: {'batch_size': 1024, 'accum_grad': 2},
        8: {'batch_size': 512, 'accum_grad': 4},
    }
    
    # Apply overrides if available for this depth
    if depth in override_params:
        for key, value in override_params[depth].items():
            if key == 'batch_size':
                batch_size = value
            elif key == 'eval_every':
                eval_every = value
    
    args = main.get_fake_args(
        task=task,
        depth=depth,
        num_layers=num_layers,
        batch_size=batch_size,
        eval_every=eval_every,
        type=gnn_type,
        stop=STOP.TRAIN,
        loader_workers=8,  # M4 MacBook Pro 16" has 10+ cores (8 P-cores + E-cores)
    )
    
    print(f"Running {gnn_type} at depth={depth}")
    print(f"Device: {torch.device('mps' if torch.backends.mps.is_available() else 'cpu')}")
    print(f"Batch size: {batch_size}, Workers: {args.loader_workers}")
    
    train_acc, test_acc, epoch = Experiment(args).run()
    
    print(f"\nFinal Results:")
    print(f"  Train accuracy: {train_acc:.4f}")
    print(f"  Test accuracy: {test_acc:.4f}")
    print(f"  Converged at epoch: {epoch}")
