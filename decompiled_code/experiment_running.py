# Reconstructed from: __pycache__/experiment.cpython-314.pyc
# What's actually running in PID 72504
# Bytecode disassembly:

"""
  0           RESUME                   0

  1           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              0 (torch)
              STORE_NAME               0 (torch)

  2           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('DataLoader',))
              IMPORT_NAME              1 (torch_geometric.data)
              IMPORT_FROM              2 (DataLoader)
              STORE_NAME               2 (DataLoader)
              POP_TOP

  3           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('ReduceLROnPlateau',))
              IMPORT_NAME              3 (torch.optim.lr_scheduler)
              IMPORT_FROM              4 (ReduceLROnPlateau)
              STORE_NAME               4 (ReduceLROnPlateau)
              POP_TOP

  5           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              5 (numpy)
              STORE_NAME               6 (np)

  6           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              7 (random)
              STORE_NAME               7 (random)

  7           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('AttrDict',))
              IMPORT_NAME              8 (attrdict)
              IMPORT_FROM              9 (AttrDict)
              STORE_NAME               9 (AttrDict)
              POP_TOP

  9           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('STOP',))
              IMPORT_NAME             10 (common)
              IMPORT_FROM             11 (STOP)
              STORE_NAME              11 (STOP)
              POP_TOP

 10           LOAD_SMALL_INT           0
              LOAD_CONST               6 (('GraphModel',))
              IMPORT_NAME             12 (models.graph_model)
              IMPORT_FROM             13 (GraphModel)
              STORE_NAME              13 (GraphModel)
              POP_TOP

 13           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST               7 (<code object Experiment at 0x1033fa9a0, file "/Users/nilscollins/Documents/TUM/bottleneck/experiment.py", line 13>)
              MAKE_FUNCTION
              LOAD_CONST               8 ('Experiment')
              CALL                     2
              STORE_NAME              14 (Experiment)
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object Experiment at 0x1033fa9a0, file "/Users/nilscollins/Documents/TUM/bottleneck/experiment.py", line 13>:
  --           MAKE_CELL                0 (__classdict__)

  13           RESUME                   0
               LOAD_NAME                0 (__name__)
               STORE_NAME               1 (__module__)
               LOAD_CONST               0 ('Experiment')
               STORE_NAME               2 (__qualname__)
               LOAD_SMALL_INT          13
               STORE_NAME               3 (__firstlineno__)
               LOAD_LOCALS
               STORE_DEREF              0 (__classdict__)

  14           LOAD_CONST               1 (<code object __init__ at 0x11284c200, file "/Users/nilscollins/Documents/TUM/bottleneck/experiment.py", line 14>)
               MAKE_FUNCTION
               STORE_NAME               4 (__init__)

  73           LOAD_CONST               2 (<code object print_args at 0x1030bf4b0, file "/Users/nilscollins/Documents/TUM/bottleneck/experiment.py", line 73>)
               MAKE_FUNCTION
               STORE_NAME               5 (print_args)

  82           LOAD_CONST               3 (<code object worker_init_fn at 0x10341dac0, file "/Users/nilscollins/Documents/TUM/bottleneck/experiment.py", line 82>)
               MAKE_FUNCTION
               STORE_NAME               6 (worker_init_fn)

  87           LOAD_CONST               4 (<code object run at 0x11282fa00, file "/Users/nilscollins/Documents/TUM/bottleneck/experiment.py", line 87>)
               MAKE_FUNCTION
               STORE_NAME               7 (run)

 181           LOAD_CONST               5 (<code object eval at 0x112035e20, file "/Users/nilscollins/Documents/TUM/bottleneck/experiment.py", line 181>)
               MAKE_FUNCTION
               STORE_NAME               8 (eval)
               LOAD_CONST               6 (('X_test', 'X_train', 'accum_grad', 'batch_size', 'criterion', 'depth', 'device', 'dim', 'eval_every', 'loader_workers', 'max_epochs', 'model', 'patience', 'seed', 'stopping_criterion', 'task', 'train_fraction', 'unroll'))
               STORE_NAME               9 (__static_attributes__)
               LOAD_FAST_BORROW         0 (__classdict__)
               STORE_NAME              10 (__classdictcell__)
               LOAD_CONST               7 (None)
               RETURN_VALUE

Disassembly of <code object __init__ at 0x11284c200, file "/Users/nilscollins/Documents/TUM/bottleneck/experi
... (truncated)
"""

