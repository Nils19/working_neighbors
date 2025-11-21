"""
Unified experiment runner for the Bottleneck repository.

This `main.py` provides a small CLI to run the three kinds of experiments contained in
the repository:
 - Tree-NeighborsMatch experiments (original `Experiment` in this repo)
 - `gnn-comparison` experiments via `gnn-comparison/Launch_Experiments.py`
 - TensorFlow `tf-gnn-samples` experiments via their runner scripts

The script intentionally delegates to the existing experiment code where possible.

Usage examples:
 - Run local Tree experiments:
     python main.py --runner tree --task DICTIONARY --depth 4 --type GGNN --batch_size 1024

 - Run gnn-comparison experiments (delegates to gnn-comparison/Launch_Experiments.py):
     python main.py --runner gnn-comparison --config gnn-comparison/config_BaselineChemical.yml --dataset ENZYMES --result-folder my_results

 - Run TF experiments (QM9 / VarMisuse):
     python main.py --runner tf --script tf-gnn-samples/run_qm9_benchs_fa.py

Notes:
 - This file attempts to be a thin orchestrator. It calls the local `Experiment` class for
   the tree experiments (the original behavior), and uses subprocess to launch scripts in
   subfolders for the other experiments so those projects keep their own CLI and configs.
 - Make sure to install dependencies for each subproject (see README files) before running.
"""

import argparse
import shlex
import subprocess
import sys
from attrdict import AttrDict

# local experiment runner
from experiment import Experiment
from common import Task, GNN_TYPE, STOP


def run_tree(args_list):
    """Run the local tree experiments using the repository's Experiment class.

    args_list is a list of strings (like sys.argv[1:]) that specify the Experiment flags.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", dest="task", default=Task.NEIGHBORS_MATCH, type=Task.from_string,
                        choices=list(Task))
    parser.add_argument("--type", dest="type", default=GNN_TYPE.GCN, type=GNN_TYPE.from_string,
                        choices=list(GNN_TYPE))
    parser.add_argument("--dim", dest="dim", default=32, type=int)
    parser.add_argument("--depth", dest="depth", default=3, type=int)
    parser.add_argument("--num_layers", dest="num_layers", default=None, type=int)
    parser.add_argument("--train_fraction", dest="train_fraction", default=0.8, type=float)
    parser.add_argument("--max_epochs", dest="max_epochs", default=50000, type=int)
    parser.add_argument("--eval_every", dest="eval_every", default=100, type=int)
    parser.add_argument("--batch_size", dest="batch_size", default=1024, type=int)
    parser.add_argument("--accum_grad", dest="accum_grad", default=1, type=int)
    parser.add_argument("--stop", dest="stop", default=STOP.TRAIN, type=STOP.from_string, choices=list(STOP))
    parser.add_argument("--patience", dest="patience", default=20, type=int)
    parser.add_argument("--loader_workers", dest="loader_workers", default=0, type=int)
    parser.add_argument('--last_layer_fully_adjacent', action='store_true')
    parser.add_argument('--no_layer_norm', action='store_true')
    parser.add_argument('--no_activation', action='store_true')
    parser.add_argument('--no_residual', action='store_true')
    parser.add_argument('--unroll', action='store_true')

    parsed = parser.parse_args(args_list)

    # Convert to AttrDict-like object expected by Experiment
    args = AttrDict({
        'task': parsed.task,
        'type': parsed.type,
        'dim': parsed.dim,
        'depth': parsed.depth,
        'num_layers': parsed.num_layers,
        'train_fraction': parsed.train_fraction,
        'max_epochs': parsed.max_epochs,
        'eval_every': parsed.eval_every,
        'batch_size': parsed.batch_size,
        'accum_grad': parsed.accum_grad,
        'stop': parsed.stop,
        'patience': parsed.patience,
        'loader_workers': parsed.loader_workers,
        'last_layer_fully_adjacent': parsed.last_layer_fully_adjacent,
        'no_layer_norm': parsed.no_layer_norm,
        'no_activation': parsed.no_activation,
        'no_residual': parsed.no_residual,
        'unroll': parsed.unroll,
    })

    Experiment(args).run()


def run_subprocess_command(cmd, cwd=None):
    """Run a command (list or string) in a subprocess and stream output."""
    if isinstance(cmd, (list, tuple)):
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd, text=True)
    else:
        proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd, text=True)

    try:
        for line in proc.stdout:
            print(line, end='')
    except KeyboardInterrupt:
        proc.kill()
        raise
    ret = proc.wait()
    if ret != 0:
        raise RuntimeError(f"Command {cmd} failed with exit code {ret}")


def run_gnn_comparison(config_file, dataset_name, result_folder, extra_args=None):
    """Delegate to gnn-comparison/Launch_Experiments.py with arguments."""
    script = 'gnn-comparison/Launch_Experiments.py'
    cmd = [sys.executable, script, '--config-file', config_file, '--dataset-name', dataset_name, '--result-folder', result_folder]
    if extra_args:
        cmd.extend(extra_args)
    run_subprocess_command(cmd, cwd='.')


def run_tf_script(script_path, extra_args=None):
    """Run a TF experiment script from tf-gnn-samples (or any path)"""
    cmd = [sys.executable, script_path]
    if extra_args:
        cmd.extend(extra_args)
    run_subprocess_command(cmd, cwd='.')


def main():
    parser = argparse.ArgumentParser(description='Unified runner for Bottleneck experiments')
    parser.add_argument('--runner', choices=['tree', 'gnn-comparison', 'tf'], default='tree',
                        help='Which subproject to run')

    # tree-specific args (collected after --)
    parser.add_argument('--config', help='config or script path for subproject runner', default=None)
    parser.add_argument('--dataset', help='dataset name for gnn-comparison', default=None)
    parser.add_argument('--result-folder', help='result folder for gnn-comparison', default='results')
    parser.add_argument('extra', nargs=argparse.REMAINDER,
                        help='Extra flags passed to the selected runner (use -- before them)')

    ns = parser.parse_args()

    if ns.runner == 'tree':
        # pass through extra args (strip leading '--' if present)
        extra = ns.extra
        if len(extra) > 0 and extra[0] == '--':
            extra = extra[1:]
        run_tree(extra)
    elif ns.runner == 'gnn-comparison':
        if ns.config is None or ns.dataset is None:
            print('For gnn-comparison runner you must supply --config and --dataset')
            sys.exit(2)
        extra = ns.extra
        if len(extra) > 0 and extra[0] == '--':
            extra = extra[1:]
        run_gnn_comparison(ns.config, ns.dataset, ns.result_folder, extra)
    else:  # tf
        if ns.config is None:
            print('For tf runner supply --config as the path to the TF script (e.g. tf-gnn-samples/run_qm9_benchs_fa.py)')
            sys.exit(2)
        extra = ns.extra
        if len(extra) > 0 and extra[0] == '--':
            extra = extra[1:]
        run_tf_script(ns.config, extra)


def get_fake_args(
        task=Task.NEIGHBORS_MATCH,
        type=GNN_TYPE.GCN,
        dim=32,
        depth=3,
        num_layers=None,
        train_fraction=0.8,
        max_epochs=50000,
        eval_every=100,
        batch_size=1024,
        accum_grad=1,
        patience=20,
        stop=STOP.TRAIN,
        loader_workers=0,
        last_layer_fully_adjacent=False,
        no_layer_norm=False,
        no_activation=False,
        no_residual=False,
        unroll=False,
):
    """Helper function for backward compatibility with run-*-2-8.py scripts.
    
    Creates an AttrDict with experiment parameters that can be passed to Experiment().
    """
    return AttrDict({
        'task': task,
        'type': type,
        'dim': dim,
        'depth': depth,
        'num_layers': num_layers,
        'train_fraction': train_fraction,
        'max_epochs': max_epochs,
        'eval_every': eval_every,
        'batch_size': batch_size,
        'accum_grad': accum_grad,
        'stop': stop,
        'patience': patience,
        'loader_workers': loader_workers,
        'last_layer_fully_adjacent': last_layer_fully_adjacent,
        'no_layer_norm': no_layer_norm,
        'no_activation': no_activation,
        'no_residual': no_residual,
        'unroll': unroll,
    })


if __name__ == '__main__':
    main()

