# Reconstructed from: tasks/__pycache__/tree_dataset.cpython-314.pyc
# Bytecode disassembly:
'''
  0           RESUME                   0

  1           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              0 (torch)
              STORE_NAME               0 (torch)

  2           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              1 (torch_geometric)
              STORE_NAME               1 (torch_geometric)

  4           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('Data',))
              IMPORT_NAME              2 (torch_geometric.data)
              IMPORT_FROM              3 (Data)
              STORE_NAME               3 (Data)
              POP_TOP

  5           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('functional',))
              IMPORT_NAME              4 (torch.nn)
              IMPORT_FROM              5 (functional)
              STORE_NAME               6 (F)
              POP_TOP

  6           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('train_test_split',))
              IMPORT_NAME              7 (sklearn.model_selection)
              IMPORT_FROM              8 (train_test_split)
              STORE_NAME               8 (train_test_split)
              POP_TOP

  9           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST               5 (<code object TreeDataset at 0x102706970, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 9>)
              MAKE_FUNCTION
              LOAD_CONST               6 ('TreeDataset')
              LOAD_NAME                9 (object)
              CALL                     3
              STORE_NAME              10 (TreeDataset)
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object TreeDataset at 0x102706970, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 9>:
  --           MAKE_CELL                0 (__class__)
               MAKE_CELL                1 (__classdict__)

   9           RESUME                   0
               LOAD_NAME                0 (__name__)
               STORE_NAME               1 (__module__)
               LOAD_CONST               0 ('TreeDataset')
               STORE_NAME               2 (__qualname__)
               LOAD_SMALL_INT           9
               STORE_NAME               3 (__firstlineno__)
               LOAD_LOCALS
               STORE_DEREF              1 (__classdict__)

  10           LOAD_FAST_BORROW         0 (__class__)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object __init__ at 0x1025071b0, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 10>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               STORE_NAME               4 (__init__)

  16           LOAD_CONST               2 (<code object add_child_edges at 0x117f55930, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 16>)
               MAKE_FUNCTION
               STORE_NAME               5 (add_child_edges)

  33           LOAD_CONST               3 (<code object _create_blank_tree at 0x1024c3730, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 33>)
               MAKE_FUNCTION
               STORE_NAME               6 (_create_blank_tree)

  38           LOAD_CONST              11 ((True,))
               LOAD_CONST               4 (<code object create_blank_tree at 0x10250e970, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 38>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME               7 (create_blank_tree)

  47           LOAD_CONST               5 (<code object generate_data at 0x117f5c7d0, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 47>)
               MAKE_FUNCTION
               STORE_NAME               8 (generate_data)

  71           LOAD_CONST               6 (<code object get_combinations at 0x10279d6f0, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 71>)
               MAKE_FUNCTION
               STORE_NAME               9 (get_combinations)

  74           LOAD_CONST               7 (<code object get_nodes_features at 0x10279e5d0, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 74>)
               MAKE_FUNCTION
               STORE_NAME              10 (get_nodes_features)

  77           LOAD_CONST               8 (<code object label at 0x10279e870, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 77>)
               MAKE_FUNCTION
               STORE_NAME              11 (label)

  80           LOAD_CONST               9 (<code object get_dims at 0x10279e790, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 80>)
               MAKE_FUNCTION
               STORE_NAME              12 (get_dims)
               LOAD_CONST              10 (('criterion', 'depth', 'edges', 'leaf_indices', 'num_nodes'))
               STORE_NAME              13 (__static_attributes__)
               LOAD_FAST_BORROW         1 (__classdict__)
               STORE_NAME              14 (__classdictcell__)
               LOAD_FAST_BORROW         0 (__class__)
               COPY                     1
               STORE_NAME              15 (__classcell__)
               RETURN_VALUE

Disassembly of <code object __init__ at 0x1025071b0, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 10>:
  --           COPY_FREE_VARS           1

  10           RESUME                   0

  11           LOAD_GLOBAL              0 (super)
               LOAD_GLOBAL              2 (TreeDataset)
               LOAD_FAST_BORROW         0 (self)
               LOAD_SUPER_ATTR         11 (__init__ + NULL|self)
               CALL                     0
               POP_TOP

  12           LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (depth, self)
               STORE_ATTR               3 (depth)

  13           LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                9 (_create_blank_tree + NULL|self)
               CALL                     0
               UNPACK_SEQUENCE          3
               LOAD_FAST_BORROW         0 (self)
               STORE_ATTR               5 (num_nodes)
               LOAD_FAST_BORROW         0 (self)
               STORE_ATTR               6 (edges)
               LOAD_FAST_BORROW         0 (self)
               STORE_ATTR               7 (leaf_indices)

  14           LOAD_GLOBAL             16 (F)
               LOAD_ATTR               18 (cross_entropy)
               LOAD_FAST_BORROW         0 (self)
               STORE_ATTR              10 (criterion)
               LOAD_CONST               0 (None)
               RETURN_VALUE

Disassembly of <code object add_child_edges at 0x117f55930, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 16>:
 16           RESUME                   0

 17           BUILD_LIST               0
              STORE_FAST               3 (edges)

 18           BUILD_LIST               0
              STORE_FAST               4 (leaf_indices)

 19           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (cur_node, max_node)
              BUILD_TUPLE              2
              BUILD_LIST               1
              STORE_FAST               5 (stack)

 20   L1:     LOAD_GLOBAL              1 (len + NULL)
              LOAD_FAST_BORROW         5 (stack)
              CALL                     1
              LOAD_SMALL_INT           0
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE      163 (to L3)
              NOT_TAKEN

 21           LOAD_FAST_BORROW         5 (stack)
              LOAD_ATTR                3 (pop + NULL|self)
              CALL                     0
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   18 (cur_node, max_node)

 22           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (cur_node, max_node)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       20 (to L2)
              NOT_TAKEN

 23           LOAD_FAST_BORROW         4 (leaf_indices)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         1 (cur_node)
              CALL                     1
              POP_TOP

 24           JUMP_BACKWARD           59 (to L1)

 25   L2:     LOAD_FAST_BORROW         1 (cur_node)
              LOAD_SMALL_INT           1
              BINARY_OP                0 (+)
              STORE_FAST               6 (left_child)

 26           LOAD_FAST_BORROW         1 (cur_node)
              LOAD_SMALL_INT           1
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (max_node, cur_node)
              BINARY_OP               10 (-)
              LOAD_SMALL_INT           2
              BINARY_OP                2 (//)
              BINARY_OP                0 (+)
              STORE_FAST               7 (right_child)

 27           LOAD_FAST_BORROW         3 (edges)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 97 (left_child, cur_node)
              BUILD_LIST               2
              CALL                     1
              POP_TOP

 28           LOAD_FAST_BORROW         3 (edges)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 113 (right_child, cur_node)
              BUILD_LIST               2
              CALL                     1
              POP_TOP

 29           LOAD_FAST_BORROW         5 (stack)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 114 (right_child, max_node)
              BUILD_TUPLE              2
              CALL                     1
              POP_TOP

 30           LOAD_FAST_BORROW         5 (stack)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (left_child, right_child)
              LOAD_SMALL_INT           1
              BINARY_OP               10 (-)
              BUILD_TUPLE              2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          178 (to L1)

 31   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (edges, leaf_indices)
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object _create_blank_tree at 0x1024c3730, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 33>:
 33           RESUME                   0

 34           LOAD_SMALL_INT           2
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (depth)
              LOAD_SMALL_INT           1
              BINARY_OP                0 (+)
              BINARY_OP                8 (**)
              LOAD_SMALL_INT           2
              BINARY_OP               10 (-)
              STORE_FAST               1 (max_node_id)

 35           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                3 (add_child_edges + NULL|self)
              LOAD_SMALL_INT           0
              LOAD_FAST_BORROW         1 (max_node_id)
              LOAD_CONST               1 (('cur_node', 'max_node'))
              CALL_KW                  2
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   35 (edges, leaf_indices)

 36           LOAD_FAST_BORROW         1 (max_node_id)
              LOAD_SMALL_INT           1
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (edges, leaf_indices)
              BUILD_TUPLE              3
              RETURN_VALUE

Disassembly of <code object create_blank_tree at 0x10250e970, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 38>:
 38           RESUME                   0

 39           LOAD_GLOBAL              0 (torch)
              LOAD_ATTR                2 (tensor)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                4 (edges)
              LOAD_GLOBAL              0 (torch)
              LOAD_ATTR                6 (long)
              LOAD_CONST               0 (('dtype',))
              CALL_KW                  2
              LOAD_ATTR                9 (t + NULL|self)
              CALL                     0
              LOAD_ATTR               11 (contiguous + NULL|self)
              CALL                     0
              STORE_FAST               2 (edge_index)

 40           LOAD_FAST_BORROW         1 (add_self_loops)
              TO_BOOL
              POP_JUMP_IF_FALSE       46 (to L1)
              NOT_TAKEN

 41           LOAD_GLOBAL             12 (torch_geometric)
              LOAD_ATTR               14 (utils)
              LOAD_ATTR               17 (add_remaining_self_loops + NULL|self)

 42           LOAD_FAST_BORROW         2 (edge_index)

 43           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               18 (num_nodes)

 41           LOAD_CONST               1 (('edge_index', 'num_nodes'))
              CALL_KW                  2
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   35 (edge_index, _)

 45   L1:     LOAD_FAST_BORROW         2 (edge_index)
              RETURN_VALUE

Disassembly of <code object generate_data at 0x117f5c7d0, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 47>:
  47           RESUME                   0

  48           BUILD_LIST               0
               STORE_FAST               2 (data_list)

  50           LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                1 (get_combinations + NULL|self)
               CALL                     0
               GET_ITER
       L1:     FOR_ITER               185 (to L2)
               STORE_FAST               3 (comb)

  51           LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                3 (create_blank_tree + NULL|self)
               LOAD_CONST               0 (True)
               LOAD_CONST               1 (('add_self_loops',))
               CALL_KW                  1
               STORE_FAST               4 (edge_index)

  52           LOAD_GLOBAL              4 (torch)
               LOAD_ATTR                6 (tensor)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                9 (get_nodes_features + NULL|self)
               LOAD_FAST_BORROW         3 (comb)
               CALL                     1
               LOAD_GLOBAL              4 (torch)
               LOAD_ATTR               10 (long)
               LOAD_CONST               2 (('dtype',))
               CALL_KW                  2
               STORE_FAST               5 (nodes)

  53           LOAD_GLOBAL              4 (torch)
               LOAD_ATTR                6 (tensor)
               PUSH_NULL
               LOAD_CONST               0 (True)
               BUILD_LIST               1
               LOAD_CONST               3 (False)
               BUILD_LIST               1
               LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         5 (nodes)
               CALL                     1
               LOAD_SMALL_INT           1
               BINARY_OP               10 (-)
               BINARY_OP                5 (*)
               BINARY_OP                0 (+)
               CALL                     1
               STORE_FAST               6 (root_mask)

  54           LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               15 (label + NULL|self)
               LOAD_FAST_BORROW         3 (comb)
               CALL                     1
               STORE_FAST               7 (label)

  55           LOAD_FAST_BORROW         2 (data_list)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (Data + NULL)

  56           LOAD_FAST_BORROW         5 (nodes)

  57           LOAD_FAST_BORROW         4 (edge_index)

  58           LOAD_FAST_BORROW         6 (root_mask)

  59           LOAD_FAST_BORROW         7 (label)

  60           LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         5 (nodes)
               CALL                     1

  55           LOAD_CONST               4 (('x', 'edge_index', 'root_mask', 'y', 'num_nodes'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          187 (to L1)

  50   L2:     END_FOR
               POP_ITER

  63           LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               21 (get_dims + NULL|self)
               CALL                     0
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST  137 (dim0, out_dim)

  64           LOAD_GLOBAL             23 (train_test_split + NULL)

  65           LOAD_FAST_LOAD_FAST     33 (data_list, train_fraction)
               LOAD_CONST               0 (True)
               LOAD_FAST_BORROW         2 (data_list)
               GET_ITER
               LOAD_FAST_AND_CLEAR     10 (data)
               SWAP                     2
       L3:     BUILD_LIST               0
               SWAP                     2
       L4:     FOR_ITER                14 (to L5)
               STORE_FAST_LOAD_FAST   170 (data, data)
               LOAD_ATTR               24 (y)
               LIST_APPEND              2
               JUMP_BACKWARD           16 (to L4)
       L5:     END_FOR
               POP_ITER
       L6:     SWAP                     2
               STORE_FAST              10 (data)

  66           LOAD_SMALL_INT          11

  64           LOAD_CONST               5 (('train_size', 'shuffle', 'stratify', 'random_state'))
               CALL_KW                  5
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST  188 (X_train, X_test)

  68           LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (X_train, X_test)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (dim0, out_dim)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               26 (criterion)
               BUILD_TUPLE              5
               RETURN_VALUE

  --   L7:     SWAP                     2
               POP_TOP

  65           SWAP                     2
               STORE_FAST              10 (data)
               RERAISE                  0
ExceptionTable:
  L3 to L6 -> L7 [7]

Disassembly of <code object get_combinations at 0x10279d6f0, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 71>:
 71           RESUME                   0

 72           LOAD_GLOBAL              0 (NotImplementedError)
              RAISE_VARARGS            1

Disassembly of <code object get_nodes_features at 0x10279e5d0, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 74>:
 74           RESUME                   0

 75           LOAD_GLOBAL              0 (NotImplementedError)
              RAISE_VARARGS            1

Disassembly of <code object label at 0x10279e870, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 77>:
 77           RESUME                   0

 78           LOAD_GLOBAL              0 (NotImplementedError)
              RAISE_VARARGS            1

Disassembly of <code object get_dims at 0x10279e790, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 80>:
 80           RESUME                   0

 81           LOAD_GLOBAL              0 (NotImplementedError)
              RAISE_VARARGS            1
'''

# Key constants:
#   0: 0
#   1: None
#   6: 'TreeDataset'

# Names used:
#   0: torch
#   1: torch_geometric
#   2: torch_geometric.data
#   3: Data
#   4: torch.nn
#   5: functional
#   6: F
#   7: sklearn.model_selection
#   8: train_test_split
#   9: object
#   10: TreeDataset
