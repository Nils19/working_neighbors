# Reconstructed from: models/__pycache__/graph_model.cpython-314.pyc
# What's actually running in PID 72504
# Bytecode disassembly:

"""
  0           RESUME                   0

  1           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              0 (torch)
              STORE_NAME               0 (torch)

  2           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('nn',))
              IMPORT_NAME              0 (torch)
              IMPORT_FROM              1 (nn)
              STORE_NAME               1 (nn)
              POP_TOP

  3           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('functional',))
              IMPORT_NAME              2 (torch.nn)
              IMPORT_FROM              3 (functional)
              STORE_NAME               4 (F)
              POP_TOP

  5           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST               4 (<code object GraphModel at 0x1033fa9a0, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 5>)
              MAKE_FUNCTION
              LOAD_CONST               5 ('GraphModel')
              LOAD_NAME                0 (torch)
              LOAD_ATTR                2 (nn)
              LOAD_ATTR               10 (Module)
              CALL                     3
              STORE_NAME               6 (GraphModel)
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object GraphModel at 0x1033fa9a0, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 5>:
  --           MAKE_CELL                0 (__class__)
               MAKE_CELL                1 (__classdict__)

   5           RESUME                   0
               LOAD_NAME                0 (__name__)
               STORE_NAME               1 (__module__)
               LOAD_CONST               0 ('GraphModel')
               STORE_NAME               2 (__qualname__)
               LOAD_SMALL_INT           5
               STORE_NAME               3 (__firstlineno__)
               LOAD_LOCALS
               STORE_DEREF              1 (__classdict__)

   6           LOAD_FAST_BORROW         0 (__class__)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object __init__ at 0x11284be00, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 6>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               STORE_NAME               4 (__init__)

  45           LOAD_CONST               2 (<code object forward at 0x11284ca00, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 45>)
               MAKE_FUNCTION
               STORE_NAME               5 (forward)

 105           LOAD_CONST               3 (<code object _make_fully_connected at 0x112035b10, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 105>)
               MAKE_FUNCTION
               STORE_NAME               6 (_make_fully_connected)
               LOAD_CONST               4 (('device', 'gnn_type', 'last_layer_fully_adjacent', 'layer0_keys', 'layer0_values', 'layer_norms', 'layers', 'num_layers', 'out_dim', 'out_layer', 'unroll', 'use_activation', 'use_layer_norm', 'use_residual'))
               STORE_NAME               7 (__static_attributes__)
               LOAD_FAST_BORROW         1 (__classdict__)
               STORE_NAME               8 (__classdictcell__)
               LOAD_FAST_BORROW         0 (__class__)
               COPY                     1
               STORE_NAME               9 (__classcell__)
               RETURN_VALUE

Disassembly of <code object __init__ at 0x11284be00, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 6>:
  --            COPY_FREE_VARS           1

   6            RESUME                   0

   8            LOAD_GLOBAL              0 (super)
                LOAD_GLOBAL              2 (GraphModel)
                LOAD_FAST_BORROW         0 (self)
                LOAD_SUPER_ATTR         11 (__init__ + NULL|self)
                CALL                     0
                POP_TOP

   9            LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (gnn_type, self)
                STORE_ATTR               3 (gnn_type)

  10            LOAD_FAST_BORROW_LOAD_FAST_BORROW 112 (unroll, self)
                STORE_ATTR               4 (unroll)

  11            LOAD_FAST_BORROW_LOAD_FAST_BORROW 96 (last_layer_fully_adjacent, self)
                STORE_ATTR               5 (last_layer_fully_adjacent)

  12            LOAD_FAST_BORROW_LOAD_FAST_BORROW 128 (layer_norm, self)
                STORE_ATTR               6 (use_layer_norm)

  13            LOAD_FAST_BORROW_LOAD_FAST_BORROW 144 (use_activation, self)
                STORE_ATTR               7 (use_activation)

  14            LOAD_FAST_BORROW_LOAD_FAST_BORROW 160 (use_residual, self)
                STORE_ATTR               8 (use_residual)

  17            LOAD_GLOBAL             18 (torch)
  
... (truncated)
"""

