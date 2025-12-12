# Reconstructed from: __pycache__/common.cpython-314.pyc
# Bytecode disassembly:
'''
  0           RESUME                   0

  1           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('Enum', 'auto'))
              IMPORT_NAME              0 (enum)
              IMPORT_FROM              1 (Enum)
              STORE_NAME               1 (Enum)
              IMPORT_FROM              2 (auto)
              STORE_NAME               2 (auto)
              POP_TOP

  3           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('TreeNeighborsMatchDataset',))
              IMPORT_NAME              3 (tasks.neighbors_match)
              IMPORT_FROM              4 (TreeNeighborsMatchDataset)
              STORE_NAME               4 (TreeNeighborsMatchDataset)
              POP_TOP

  4           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('DictionaryLookupDataset',))
              IMPORT_NAME              5 (tasks.dictionary_lookup)
              IMPORT_FROM              6 (DictionaryLookupDataset)
              STORE_NAME               6 (DictionaryLookupDataset)
              POP_TOP

  6           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('nn',))
              IMPORT_NAME              7 (torch)
              IMPORT_FROM              8 (nn)
              STORE_NAME               8 (nn)
              POP_TOP

  7           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('GCNConv', 'GatedGraphConv', 'GINConv', 'GATConv'))
              IMPORT_NAME              9 (torch_geometric.nn)
              IMPORT_FROM             10 (GCNConv)
              STORE_NAME              10 (GCNConv)
              IMPORT_FROM             11 (GatedGraphConv)
              STORE_NAME              11 (GatedGraphConv)
              IMPORT_FROM             12 (GINConv)
              STORE_NAME              12 (GINConv)
              IMPORT_FROM             13 (GATConv)
              STORE_NAME              13 (GATConv)
              POP_TOP

 10           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST               6 (<code object Task at 0x1027ae670, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 10>)
              MAKE_FUNCTION
              LOAD_CONST               7 ('Task')
              LOAD_NAME                1 (Enum)
              CALL                     3
              STORE_NAME              14 (Task)

 29           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST               8 (<code object GNN_TYPE at 0x102706970, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 29>)
              MAKE_FUNCTION
              LOAD_CONST               9 ('GNN_TYPE')
              LOAD_NAME                1 (Enum)
              CALL                     3
              STORE_NAME              15 (GNN_TYPE)

 59           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST              10 (<code object STOP at 0x1027ae1f0, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 59>)
              MAKE_FUNCTION
              LOAD_CONST              11 ('STOP')
              LOAD_NAME                1 (Enum)
              CALL                     3
              STORE_NAME              16 (STOP)

 71           LOAD_CONST              12 (<code object one_hot at 0x10253d920, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 71>)
              MAKE_FUNCTION
              STORE_NAME              17 (one_hot)
              LOAD_CONST              13 (None)
              RETURN_VALUE

Disassembly of <code object Task at 0x1027ae670, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 10>:
  --           MAKE_CELL                0 (__classdict__)

  10           RESUME                   0
               LOAD_NAME                0 (__name__)
               STORE_NAME               1 (__module__)
               LOAD_CONST               0 ('Task')
               STORE_NAME               2 (__qualname__)
               LOAD_SMALL_INT          10
               STORE_NAME               3 (__firstlineno__)
               LOAD_LOCALS
               STORE_DEREF              0 (__classdict__)

  11           LOAD_NAME                4 (auto)
               PUSH_NULL
               CALL                     0
               STORE_NAME               5 (NEIGHBORS_MATCH)

  13           LOAD_NAME                6 (staticmethod)

  14           LOAD_CONST               1 (<code object from_string at 0x1027ae430, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 13>)
               MAKE_FUNCTION

  13           CALL                     0

  14           STORE_NAME               7 (from_string)

  20           LOAD_CONST               2 (<code object get_dataset at 0x102707730, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 20>)
               MAKE_FUNCTION
               STORE_NAME               8 (get_dataset)
               LOAD_CONST               3 (())
               STORE_NAME               9 (__static_attributes__)
               LOAD_FAST_BORROW         0 (__classdict__)
               STORE_NAME              10 (__classdictcell__)
               LOAD_CONST               4 (None)
               RETURN_VALUE

Disassembly of <code object from_string at 0x1027ae430, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 13>:
  13           RESUME                   0

  15           NOP

  16   L1:     LOAD_GLOBAL              0 (Task)
               LOAD_FAST_BORROW         0 (s)
               BINARY_OP               26 ([])
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  17           LOAD_GLOBAL              2 (KeyError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       12 (to L4)
               NOT_TAKEN
               POP_TOP

  18           LOAD_GLOBAL              5 (ValueError + NULL)
               CALL                     0
               RAISE_VARARGS            1

  17   L4:     RERAISE                  0

  --   L5:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L5 -> L5 [1] lasti

Disassembly of <code object get_dataset at 0x102707730, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 20>:
 20           RESUME                   0

 21           LOAD_FAST_BORROW         0 (self)
              LOAD_GLOBAL              0 (Task)
              LOAD_ATTR                2 (NEIGHBORS_MATCH)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       13 (to L1)
              NOT_TAKEN

 22           LOAD_GLOBAL              5 (DictionaryLookupDataset + NULL)
              LOAD_FAST_BORROW         1 (depth)
              CALL                     1
              STORE_FAST               3 (dataset)
              JUMP_FORWARD             2 (to L2)

 24   L1:     LOAD_CONST               0 (None)
              STORE_FAST               3 (dataset)

 26   L2:     LOAD_FAST_BORROW         3 (dataset)
              LOAD_ATTR                7 (generate_data + NULL|self)
              LOAD_FAST_BORROW         2 (train_fraction)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object GNN_TYPE at 0x102706970, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 29>:
  --           MAKE_CELL                0 (__classdict__)

  29           RESUME                   0
               LOAD_NAME                0 (__name__)
               STORE_NAME               1 (__module__)
               LOAD_CONST               0 ('GNN_TYPE')
               STORE_NAME               2 (__qualname__)
               LOAD_SMALL_INT          29
               STORE_NAME               3 (__firstlineno__)
               LOAD_LOCALS
               STORE_DEREF              0 (__classdict__)

  30           LOAD_NAME                4 (auto)
               PUSH_NULL
               CALL                     0
               STORE_NAME               5 (GCN)

  31           LOAD_NAME                4 (auto)
               PUSH_NULL
               CALL                     0
               STORE_NAME               6 (GGNN)

  32           LOAD_NAME                4 (auto)
               PUSH_NULL
               CALL                     0
               STORE_NAME               7 (GIN)

  33           LOAD_NAME                4 (auto)
               PUSH_NULL
               CALL                     0
               STORE_NAME               8 (GAT)

  35           LOAD_NAME                9 (staticmethod)

  36           LOAD_CONST               1 (<code object from_string at 0x1027ae310, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 35>)
               MAKE_FUNCTION

  35           CALL                     0

  36           STORE_NAME              10 (from_string)

  42           LOAD_CONST               2 (<code object get_layer at 0x102a04830, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 42>)
               MAKE_FUNCTION
               STORE_NAME              11 (get_layer)
               LOAD_CONST               3 (())
               STORE_NAME              12 (__static_attributes__)
               LOAD_FAST_BORROW         0 (__classdict__)
               STORE_NAME              13 (__classdictcell__)
               LOAD_CONST               4 (None)
               RETURN_VALUE

Disassembly of <code object from_string at 0x1027ae310, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 35>:
  35           RESUME                   0

  37           NOP

  38   L1:     LOAD_GLOBAL              0 (GNN_TYPE)
               LOAD_FAST_BORROW         0 (s)
               BINARY_OP               26 ([])
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  39           LOAD_GLOBAL              2 (KeyError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       12 (to L4)
               NOT_TAKEN
               POP_TOP

  40           LOAD_GLOBAL              5 (ValueError + NULL)
               CALL                     0
               RAISE_VARARGS            1

  39   L4:     RERAISE                  0

  --   L5:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L5 -> L5 [1] lasti

Disassembly of <code object get_layer at 0x102a04830, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 42>:
 42           RESUME                   0

 43           LOAD_FAST_BORROW         0 (self)
              LOAD_GLOBAL              0 (GNN_TYPE)
              LOAD_ATTR                2 (GCN)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       14 (to L1)
              NOT_TAKEN

 44           LOAD_GLOBAL              5 (GCNConv + NULL)

 45           LOAD_FAST_BORROW         1 (in_dim)

 46           LOAD_FAST_BORROW         2 (out_dim)

 44           LOAD_CONST               0 (('in_channels', 'out_channels'))
              CALL_KW                  2
              RETURN_VALUE

 47   L1:     LOAD_FAST_BORROW         0 (self)
              LOAD_GLOBAL              0 (GNN_TYPE)
              LOAD_ATTR                6 (GGNN)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       14 (to L2)
              NOT_TAKEN

 48           LOAD_GLOBAL              9 (GatedGraphConv + NULL)
              LOAD_FAST_BORROW         2 (out_dim)
              LOAD_SMALL_INT           1
              LOAD_CONST               1 (('out_channels', 'num_layers'))
              CALL_KW                  2
              RETURN_VALUE

 49   L2:     LOAD_FAST_BORROW         0 (self)
              LOAD_GLOBAL              0 (GNN_TYPE)
              LOAD_ATTR               10 (GIN)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE      155 (to L3)
              NOT_TAKEN

 50           LOAD_GLOBAL             13 (GINConv + NULL)
              LOAD_GLOBAL             14 (nn)
              LOAD_ATTR               16 (Sequential)
              PUSH_NULL
              LOAD_GLOBAL             14 (nn)
              LOAD_ATTR               18 (Linear)
              PUSH_NULL
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (in_dim, out_dim)
              CALL                     2
              LOAD_GLOBAL             14 (nn)
              LOAD_ATTR               20 (BatchNorm1d)
              PUSH_NULL
              LOAD_FAST_BORROW         2 (out_dim)
              CALL                     1
              LOAD_GLOBAL             14 (nn)
              LOAD_ATTR               22 (ReLU)
              PUSH_NULL
              CALL                     0

 51           LOAD_GLOBAL             14 (nn)
              LOAD_ATTR               18 (Linear)
              PUSH_NULL
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 34 (out_dim, out_dim)
              CALL                     2
              LOAD_GLOBAL             14 (nn)
              LOAD_ATTR               20 (BatchNorm1d)
              PUSH_NULL
              LOAD_FAST_BORROW         2 (out_dim)
              CALL                     1
              LOAD_GLOBAL             14 (nn)
              LOAD_ATTR               22 (ReLU)
              PUSH_NULL
              CALL                     0

 50           CALL                     6
              CALL                     1
              RETURN_VALUE

 52   L3:     LOAD_FAST_BORROW         0 (self)
              LOAD_GLOBAL              0 (GNN_TYPE)
              LOAD_ATTR               24 (GAT)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       23 (to L4)
              NOT_TAKEN

 55           LOAD_SMALL_INT           4
              STORE_FAST               3 (num_heads)

 56           LOAD_GLOBAL             27 (GATConv + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (in_dim, out_dim)
              LOAD_FAST_BORROW         3 (num_heads)
              BINARY_OP                2 (//)
              LOAD_FAST_BORROW         3 (num_heads)
              LOAD_CONST               2 (('heads',))
              CALL_KW                  3
              RETURN_VALUE

 52   L4:     LOAD_CONST               3 (None)
              RETURN_VALUE

Disassembly of <code object STOP at 0x1027ae1f0, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 59>:
  --           MAKE_CELL                0 (__classdict__)

  59           RESUME                   0
               LOAD_NAME                0 (__name__)
               STORE_NAME               1 (__module__)
               LOAD_CONST               0 ('STOP')
               STORE_NAME               2 (__qualname__)
               LOAD_SMALL_INT          59
               STORE_NAME               3 (__firstlineno__)
               LOAD_LOCALS
               STORE_DEREF              0 (__classdict__)

  60           LOAD_NAME                4 (auto)
               PUSH_NULL
               CALL                     0
               STORE_NAME               5 (TRAIN)

  61           LOAD_NAME                4 (auto)
               PUSH_NULL
               CALL                     0
               STORE_NAME               6 (TEST)

  63           LOAD_NAME                7 (staticmethod)

  64           LOAD_CONST               1 (<code object from_string at 0x1027ad8f0, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 63>)
               MAKE_FUNCTION

  63           CALL                     0

  64           STORE_NAME               8 (from_string)
               LOAD_CONST               2 (())
               STORE_NAME               9 (__static_attributes__)
               LOAD_FAST_BORROW         0 (__classdict__)
               STORE_NAME              10 (__classdictcell__)
               LOAD_CONST               3 (None)
               RETURN_VALUE

Disassembly of <code object from_string at 0x1027ad8f0, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 63>:
  63           RESUME                   0

  65           NOP

  66   L1:     LOAD_GLOBAL              0 (STOP)
               LOAD_FAST_BORROW         0 (s)
               BINARY_OP               26 ([])
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  67           LOAD_GLOBAL              2 (KeyError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       12 (to L4)
               NOT_TAKEN
               POP_TOP

  68           LOAD_GLOBAL              5 (ValueError + NULL)
               CALL                     0
               RAISE_VARARGS            1

  67   L4:     RERAISE                  0

  --   L5:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L5 -> L5 [1] lasti

Disassembly of <code object one_hot at 0x10253d920, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 71>:
  71           RESUME                   0

  72           LOAD_GLOBAL              1 (range + NULL)
               LOAD_FAST_BORROW         1 (depth)
               CALL                     1
               GET_ITER
               LOAD_FAST_AND_CLEAR      2 (i)
               SWAP                     2
       L1:     BUILD_LIST               0
               SWAP                     2
       L2:     FOR_ITER                13 (to L5)
               STORE_FAST_LOAD_FAST    34 (i, i)
               LOAD_FAST_BORROW         0 (key)
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_SMALL_INT           1
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_SMALL_INT           0
       L4:     LIST_APPEND              2
               JUMP_BACKWARD           15 (to L2)
       L5:     END_FOR
               POP_ITER
       L6:     SWAP                     2
               STORE_FAST               2 (i)
               RETURN_VALUE

  --   L7:     SWAP                     2
               POP_TOP

  72           SWAP                     2
               STORE_FAST               2 (i)
               RERAISE                  0
ExceptionTable:
  L1 to L6 -> L7 [2]
'''

# Key constants:
#   0: 0
#   7: 'Task'
#   9: 'GNN_TYPE'
#   11: 'STOP'
#   13: None

# Names used:
#   0: enum
#   1: Enum
#   2: auto
#   3: tasks.neighbors_match
#   4: TreeNeighborsMatchDataset
#   5: tasks.dictionary_lookup
#   6: DictionaryLookupDataset
#   7: torch
#   8: nn
#   9: torch_geometric.nn
#   10: GCNConv
#   11: GatedGraphConv
#   12: GINConv
#   13: GATConv
#   14: Task
#   15: GNN_TYPE
#   16: STOP
#   17: one_hot
