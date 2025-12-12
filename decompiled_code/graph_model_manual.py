# Reconstructed from: models/__pycache__/graph_model.cpython-314.pyc
# Bytecode disassembly:
'''
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
              LOAD_CONST               4 (<code object GraphModel at 0x1027d69a0, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 5>)
              MAKE_FUNCTION
              LOAD_CONST               5 ('GraphModel')
              LOAD_NAME                0 (torch)
              LOAD_ATTR                2 (nn)
              LOAD_ATTR               10 (Module)
              CALL                     3
              STORE_NAME               6 (GraphModel)
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object GraphModel at 0x1027d69a0, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 5>:
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
               LOAD_CONST               1 (<code object __init__ at 0x10400e000, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 6>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               STORE_NAME               4 (__init__)

  45           LOAD_CONST               2 (<code object forward at 0x10400ec00, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 45>)
               MAKE_FUNCTION
               STORE_NAME               5 (forward)

 105           LOAD_CONST               3 (<code object _make_fully_connected at 0x102a04100, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 105>)
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

Disassembly of <code object __init__ at 0x10400e000, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 6>:
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
                LOAD_ATTR               20 (cuda)
                LOAD_ATTR               23 (is_available + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       29 (to L1)
                NOT_TAKEN

  18            LOAD_GLOBAL             18 (torch)
                LOAD_ATTR               24 (device)
                PUSH_NULL
                LOAD_CONST               0 ('cuda')
                CALL                     1
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR              12 (device)
                JUMP_FORWARD           133 (to L3)

  19    L1:     LOAD_GLOBAL             27 (hasattr + NULL)
                LOAD_GLOBAL             18 (torch)
                LOAD_ATTR               28 (backends)
                LOAD_CONST               1 ('mps')
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       75 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL             18 (torch)
                LOAD_ATTR               28 (backends)
                LOAD_ATTR               30 (mps)
                LOAD_ATTR               23 (is_available + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       29 (to L2)
                NOT_TAKEN

  20            LOAD_GLOBAL             18 (torch)
                LOAD_ATTR               24 (device)
                PUSH_NULL
                LOAD_CONST               1 ('mps')
                CALL                     1
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR              12 (device)
                JUMP_FORWARD            27 (to L3)

  22    L2:     LOAD_GLOBAL             18 (torch)
                LOAD_ATTR               24 (device)
                PUSH_NULL
                LOAD_CONST               2 ('cpu')
                CALL                     1
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR              12 (device)

  24    L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (num_layers, self)
                STORE_ATTR              16 (num_layers)

  27            LOAD_GLOBAL             34 (nn)
                LOAD_ATTR               36 (Embedding)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (dim0)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_BORROW         4 (h_dim)
                LOAD_CONST               3 (('num_embeddings', 'embedding_dim'))
                CALL_KW                  2
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR              19 (layer0_keys)

  28            LOAD_GLOBAL             34 (nn)
                LOAD_ATTR               36 (Embedding)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (dim0)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_BORROW         4 (h_dim)
                LOAD_CONST               3 (('num_embeddings', 'embedding_dim'))
                CALL_KW                  2
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR              20 (layer0_values)

  30            LOAD_GLOBAL             34 (nn)
                LOAD_ATTR               42 (ModuleList)
                PUSH_NULL
                CALL                     0
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR              22 (layers)

  31            LOAD_GLOBAL             34 (nn)
                LOAD_ATTR               42 (ModuleList)
                PUSH_NULL
                CALL                     0
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR              23 (layer_norms)

  32            LOAD_FAST_BORROW         7 (unroll)
                TO_BOOL
                POP_JUMP_IF_FALSE       45 (to L4)
                NOT_TAKEN

  33            LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               44 (layers)
                LOAD_ATTR               49 (append + NULL|self)
                LOAD_FAST_BORROW         1 (gnn_type)
                LOAD_ATTR               51 (get_layer + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 68 (h_dim, h_dim)
                LOAD_CONST               4 (('in_dim', 'out_dim'))
                CALL_KW                  2
                CALL                     1
                POP_TOP
                JUMP_FORWARD            61 (to L7)

  35    L4:     LOAD_GLOBAL             53 (range + NULL)
                LOAD_FAST_BORROW         2 (num_layers)
                CALL                     1
                GET_ITER
        L5:     FOR_ITER                46 (to L6)
                STORE_FAST              11 (i)

  36            LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               44 (layers)
                LOAD_ATTR               49 (append + NULL|self)
                LOAD_FAST_BORROW         1 (gnn_type)
                LOAD_ATTR               51 (get_layer + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 68 (h_dim, h_dim)
                LOAD_CONST               4 (('in_dim', 'out_dim'))
                CALL_KW                  2
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           48 (to L5)

  35    L6:     END_FOR
                POP_ITER

  38    L7:     LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               12 (use_layer_norm)
                TO_BOOL
                POP_JUMP_IF_FALSE       66 (to L10)
                NOT_TAKEN

  39            LOAD_GLOBAL             53 (range + NULL)
                LOAD_FAST_BORROW         2 (num_layers)
                CALL                     1
                GET_ITER
        L8:     FOR_ITER                50 (to L9)
                STORE_FAST              11 (i)

  40            LOAD_FAST_BORROW         0 (self)
                LOAD_ATTR               46 (layer_norms)
                LOAD_ATTR               49 (append + NULL|self)
                LOAD_GLOBAL             34 (nn)
                LOAD_ATTR               54 (LayerNorm)
                PUSH_NULL
                LOAD_FAST_BORROW         4 (h_dim)
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           52 (to L8)

  39    L9:     END_FOR
                POP_ITER

  42   L10:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 80 (out_dim, self)
                STORE_ATTR              28 (out_dim)

  43            LOAD_GLOBAL             34 (nn)
                LOAD_ATTR               58 (Linear)
                PUSH_NULL
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (h_dim, out_dim)
                LOAD_CONST               5 (False)
                LOAD_CONST               6 (('in_features', 'out_features', 'bias'))
                CALL_KW                  3
                LOAD_FAST_BORROW         0 (self)
                STORE_ATTR              30 (out_layer)
                LOAD_CONST               7 (None)
                RETURN_VALUE

Disassembly of <code object forward at 0x10400ec00, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 45>:
 45            RESUME                   0

 46            LOAD_FAST_BORROW         1 (data)
               LOAD_ATTR                0 (x)
               LOAD_FAST_BORROW         1 (data)
               LOAD_ATTR                2 (edge_index)
               LOAD_FAST_BORROW         1 (data)
               LOAD_ATTR                4 (batch)
               STORE_FAST_STORE_FAST   67 (batch, edge_index)
               STORE_FAST               2 (x)

 49            LOAD_GLOBAL              7 (hasattr + NULL)
               LOAD_FAST_BORROW         1 (data)
               LOAD_CONST               0 ('root_mask')
               CALL                     2
               STORE_FAST               5 (is_tree_task)

 51            LOAD_FAST_BORROW         5 (is_tree_task)
               TO_BOOL
               POP_JUMP_IF_FALSE       73 (to L1)
               NOT_TAKEN

 52            LOAD_FAST_BORROW         1 (data)
               LOAD_ATTR                8 (root_mask)
               STORE_FAST               6 (roots)

 54            LOAD_FAST_BORROW         2 (x)
               LOAD_CONST               5 ((slice(None, None, None), 0))
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW         2 (x)
               LOAD_CONST               6 ((slice(None, None, None), 1))
               BINARY_OP               26 ([])
               STORE_FAST_STORE_FAST  135 (x_val, x_key)

 55            LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               11 (layer0_keys + NULL|self)
               LOAD_FAST_BORROW         7 (x_key)
               CALL                     1
               STORE_FAST               9 (x_key_embed)

 56            LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               13 (layer0_values + NULL|self)
               LOAD_FAST_BORROW         8 (x_val)
               CALL                     1
               STORE_FAST              10 (x_val_embed)

 57            LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (x_key_embed, x_val_embed)
               BINARY_OP                0 (+)
               STORE_FAST               2 (x)
               JUMP_FORWARD            59 (to L2)

 60    L1:     LOAD_FAST_BORROW         2 (x)
               LOAD_CONST               5 ((slice(None, None, None), 0))
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW         2 (x)
               LOAD_CONST               6 ((slice(None, None, None), 1))
               BINARY_OP               26 ([])
               STORE_FAST_STORE_FAST  135 (x_val, x_key)

 61            LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               11 (layer0_keys + NULL|self)
               LOAD_FAST_BORROW         7 (x_key)
               CALL                     1
               STORE_FAST               9 (x_key_embed)

 62            LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               13 (layer0_values + NULL|self)
               LOAD_FAST_BORROW         8 (x_val)
               CALL                     1
               STORE_FAST              10 (x_val_embed)

 63            LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (x_key_embed, x_val_embed)
               BINARY_OP                0 (+)
               STORE_FAST               2 (x)

 66    L2:     LOAD_GLOBAL             15 (range + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               16 (num_layers)
               CALL                     1
               GET_ITER
       L3:     EXTENDED_ARG             1
               FOR_ITER               408 (to L13)
               STORE_FAST              11 (i)

 67            LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               18 (unroll)
               TO_BOOL
               POP_JUMP_IF_FALSE       21 (to L4)
               NOT_TAKEN

 68            LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               20 (layers)
               LOAD_SMALL_INT           0
               BINARY_OP               26 ([])
               STORE_FAST              12 (layer)
               JUMP_FORWARD            19 (to L5)

 70    L4:     LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               20 (layers)
               LOAD_FAST_BORROW        11 (i)
               BINARY_OP               26 ([])
               STORE_FAST              12 (layer)

 72    L5:     LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               22 (last_layer_fully_adjacent)
               TO_BOOL
               POP_JUMP_IF_FALSE      203 (to L7)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 176 (i, self)
               LOAD_ATTR               16 (num_layers)
               LOAD_SMALL_INT           1
               BINARY_OP               10 (-)
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE      180 (to L7)
               NOT_TAKEN

 73            LOAD_FAST_BORROW         5 (is_tree_task)
               TO_BOOL
               POP_JUMP_IF_FALSE      143 (to L6)
               NOT_TAKEN

 74            LOAD_GLOBAL             24 (torch)
               LOAD_ATTR               26 (nonzero)
               PUSH_NULL
               LOAD_FAST_CHECK          6 (roots)
               LOAD_CONST               1 (False)
               LOAD_CONST               2 (('as_tuple',))
               CALL_KW                  2
               LOAD_ATTR               29 (squeeze + NULL|self)
               LOAD_CONST               7 (-1)
               CALL                     1
               STORE_FAST              13 (root_indices)

 75            LOAD_FAST_BORROW        13 (root_indices)
               LOAD_ATTR               31 (index_select + NULL|self)
               LOAD_SMALL_INT           0
               LOAD_FAST_BORROW         4 (batch)
               LOAD_CONST               3 (('dim', 'index'))
               CALL_KW                  2
               STORE_FAST              14 (target_roots)

 76            LOAD_GLOBAL             24 (torch)
               LOAD_ATTR               32 (arange)
               PUSH_NULL
               LOAD_SMALL_INT           0
               LOAD_FAST_BORROW         1 (data)
               LOAD_ATTR               34 (num_nodes)
               CALL                     2
               LOAD_ATTR               37 (to + NULL|self)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               38 (device)
               CALL                     1
               STORE_FAST              15 (source_nodes)

 77            LOAD_GLOBAL             24 (torch)
               LOAD_ATTR               40 (stack)
               PUSH_NULL
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 254 (source_nodes, target_roots)
               BUILD_LIST               2
               LOAD_SMALL_INT           0
               LOAD_CONST               4 (('dim',))
               CALL_KW                  2
               STORE_FAST              16 (edges)
               JUMP_FORWARD            31 (to L8)

 79    L6:     LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               43 (_make_fully_connected + NULL|self)
               LOAD_FAST_BORROW         1 (data)
               LOAD_ATTR               34 (num_nodes)
               LOAD_FAST_BORROW         4 (batch)
               CALL                     2
               STORE_FAST              16 (edges)
               JUMP_FORWARD             2 (to L8)

 81    L7:     LOAD_FAST                3 (edge_index)
               STORE_FAST              16 (edges)

 83    L8:     LOAD_FAST_BORROW        12 (layer)
               PUSH_NULL
               LOAD_FAST_BORROW         2 (x)
               LOAD_FAST_BORROW        16 (edges)
               CALL                     2
               STORE_FAST              17 (new_x)

 85            LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               44 (use_activation)
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L9)
               NOT_TAKEN

 86            LOAD_GLOBAL             46 (F)
               LOAD_ATTR               48 (relu)
               PUSH_NULL
               LOAD_FAST_BORROW        17 (new_x)
               CALL                     1
               STORE_FAST              17 (new_x)

 88    L9:     LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               50 (use_residual)
               TO_BOOL
               POP_JUMP_IF_FALSE       11 (to L10)
               NOT_TAKEN

 89            LOAD_FAST_BORROW         2 (x)
               LOAD_FAST_BORROW        17 (new_x)
               BINARY_OP                0 (+)
               STORE_FAST               2 (x)
               JUMP_FORWARD             2 (to L11)

 91   L10:     LOAD_FAST               17 (new_x)
               STORE_FAST               2 (x)

 93   L11:     LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               52 (use_layer_norm)
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L12)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          383 (to L3)

 94   L12:     LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               54 (layer_norms)
               LOAD_FAST_BORROW        11 (i)
               BINARY_OP               26 ([])
               PUSH_NULL
               LOAD_FAST_BORROW         2 (x)
               CALL                     1
               STORE_FAST               2 (x)
               EXTENDED_ARG             1
               JUMP_BACKWARD          411 (to L3)

 66   L13:     END_FOR
               POP_ITER

 97            LOAD_FAST_BORROW         5 (is_tree_task)
               TO_BOOL
               POP_JUMP_IF_FALSE       29 (to L14)
               NOT_TAKEN

 98            LOAD_FAST_BORROW         2 (x)
               LOAD_FAST_CHECK          6 (roots)
               BINARY_OP               26 ([])
               STORE_FAST              18 (root_nodes)

 99            LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               57 (out_layer + NULL|self)
               LOAD_FAST_BORROW        18 (root_nodes)
               CALL                     1
               STORE_FAST              19 (logits)

103            LOAD_FAST_BORROW        19 (logits)
               RETURN_VALUE

101   L14:     LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               57 (out_layer + NULL|self)
               LOAD_FAST_BORROW         2 (x)
               CALL                     1
               STORE_FAST              19 (logits)

103            LOAD_FAST_BORROW        19 (logits)
               RETURN_VALUE

Disassembly of <code object _make_fully_connected at 0x102a04100, file "/Users/nilscollins/Documents/TUM/bottleneck/models/graph_model.py", line 105>:
105           RESUME                   0

107           BUILD_LIST               0
              STORE_FAST               3 (edges)

109           LOAD_GLOBAL              0 (torch)
              LOAD_ATTR                2 (unique)
              PUSH_NULL
              LOAD_FAST_BORROW         2 (batch)
              CALL                     1
              STORE_FAST               4 (unique_batches)

111           LOAD_FAST_BORROW         4 (unique_batches)
              GET_ITER
      L1:     FOR_ITER               119 (to L7)
              STORE_FAST               5 (batch_idx)

112           LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (batch, batch_idx)
              COMPARE_OP              72 (==)
              STORE_FAST               6 (node_mask)

113           LOAD_GLOBAL              0 (torch)
              LOAD_ATTR                4 (nonzero)
              PUSH_NULL
              LOAD_FAST_BORROW         6 (node_mask)
              LOAD_CONST               1 (False)
              LOAD_CONST               2 (('as_tuple',))
              CALL_KW                  2
              LOAD_ATTR                7 (squeeze + NULL|self)
              LOAD_CONST               4 (-1)
              CALL                     1
              STORE_FAST               7 (graph_nodes)

115           LOAD_FAST_BORROW         7 (graph_nodes)
              GET_ITER
      L2:     FOR_ITER                67 (to L6)
              STORE_FAST               8 (i)

116           LOAD_FAST_BORROW         7 (graph_nodes)
              GET_ITER
      L3:     FOR_ITER                58 (to L5)
              STORE_FAST               9 (j)

117           LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (i, j)
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L3)

118   L4:     LOAD_FAST_BORROW         3 (edges)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_FAST_BORROW         8 (i)
              LOAD_ATTR               11 (item + NULL|self)
              CALL                     0
              LOAD_FAST_BORROW         9 (j)
              LOAD_ATTR               11 (item + NULL|self)
              CALL                     0
              BUILD_LIST               2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           60 (to L3)

116   L5:     END_FOR
              POP_ITER
              JUMP_BACKWARD           69 (to L2)

115   L6:     END_FOR
              POP_ITER
              JUMP_BACKWARD          121 (to L1)

111   L7:     END_FOR
              POP_ITER

120           LOAD_GLOBAL             13 (len + NULL)
              LOAD_FAST_BORROW         3 (edges)
              CALL                     1
              LOAD_SMALL_INT           0
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        7 (to L8)
              NOT_TAKEN

121           LOAD_GLOBAL             14 (edge_index)
              RETURN_VALUE

123   L8:     LOAD_GLOBAL              0 (torch)
              LOAD_ATTR               16 (tensor)
              PUSH_NULL
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 48 (edges, self)
              LOAD_ATTR               18 (device)
              LOAD_CONST               3 (('device',))
              CALL_KW                  2
              LOAD_ATTR               21 (t + NULL|self)
              CALL                     0
              RETURN_VALUE
'''

# Key constants:
#   0: 0
#   1: None
#   5: 'GraphModel'

# Names used:
#   0: torch
#   1: nn
#   2: torch.nn
#   3: functional
#   4: F
#   5: Module
#   6: GraphModel
