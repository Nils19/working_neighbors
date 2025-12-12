# Decompiled Code from Running Process (PID 72504)

## What's in this directory

This contains the **exact code** that's executing in the running GAT training process.

## Bytecode Cache Timestamps

- `dictionary_lookup.cpython-314.pyc`: Dec 11 19:48 (recompiled during run)
- `tree_dataset.cpython-314.pyc`: Dec 11 19:43 (right before run started)
- `experiment.cpython-314.pyc`: Dec 10 18:31
- `common.cpython-314.pyc`: Dec 11 08:20
- `graph_model.cpython-314.pyc`: Dec 11 08:20

Training started: Dec 11 19:45:20

## Files

### Bytecode Analysis (what's actually executing):
- `*_running.py` - Bytecode disassembly from .pyc files
- `*_bytecode.txt` - Full bytecode disassembly
- `*_bytecode_full.txt` - Extended bytecode analysis

### Source Code (reconstructed):
- `*_actual.py` - The actual source code that was compiled into the running bytecode

## Key Finding: Label Function

From bytecode analysis, the label function contains BOTH subtractions:
\`\`\`python
def label(self, combination):
    selected_key, values = combination
    return int(values[selected_key - 1]) - 1
\`\`\`

The "- 1" fix IS present in the running code.
