#!/bin/bash
#SBATCH -p lrz-hgx-h100-94x4                   # GPU partition (H100)
#SBATCH --gres=gpu:1                           # 1 GPU
#SBATCH -t 12:00:00                            # time limit
#SBATCH -J qm9_fa                              # job name
#SBATCH -o qm9_%j.out                          # stdout log
#SBATCH -e qm9_%j.err                          # stderr log
#SBATCH --container-image=nvcr.io/nvidia/tensorflow:23.01-tf1-py3
#SBATCH --container-mounts=/dss/dsshome1/lxc0B/apdl017/paper-05/nils/graph:/workspace

cd /workspace

# Optional: install extra deps if tf-gnn-samples has a requirements file
if [ -f tf-gnn-samples/requirements.txt ]; then
  pip install -r tf-gnn-samples/requirements.txt
fi

# Run QM9 experiment
python tf-gnn-samples/run_qm9_benchs_fa.py >> /workspace/qm9_results.txt 2>&1

