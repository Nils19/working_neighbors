# Reconstructed from: tasks/__pycache__/dictionary_lookup.cpython-314.pyc
# Bytecode disassembly:
'''
  0           RESUME                   0

  1           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              0 (numpy)
              STORE_NAME               1 (np)

  2           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              2 (itertools)
              STORE_NAME               2 (itertools)

  3           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              3 (random)
              STORE_NAME               3 (random)

  4           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              4 (math)
              STORE_NAME               4 (math)

  6           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('TreeDataset',))
              IMPORT_NAME              5 (tasks.tree_dataset)
              IMPORT_FROM              6 (TreeDataset)
              STORE_NAME               6 (TreeDataset)
              POP_TOP

  7           LOAD_SMALL_INT           0
              LOAD_CONST               1 (None)
              IMPORT_NAME              7 (common)
              STORE_NAME               7 (common)

 10           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST               3 (<code object DictionaryLookupDataset at 0x1027ae310, file "tasks/dictionary_lookup.py", line 10>)
              MAKE_FUNCTION
              LOAD_CONST               4 ('DictionaryLookupDataset')
              LOAD_NAME                6 (TreeDataset)
              CALL                     3
              STORE_NAME               8 (DictionaryLookupDataset)
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object DictionaryLookupDataset at 0x1027ae310, file "tasks/dictionary_lookup.py", line 10>:
  --           MAKE_CELL                0 (__class__)
               MAKE_CELL                1 (__classdict__)

  10           RESUME                   0
               LOAD_NAME                0 (__name__)
               STORE_NAME               1 (__module__)
               LOAD_CONST               0 ('DictionaryLookupDataset')
               STORE_NAME               2 (__qualname__)
               LOAD_SMALL_INT          10
               STORE_NAME               3 (__firstlineno__)
               LOAD_LOCALS
               STORE_DEREF              1 (__classdict__)

  11           LOAD_FAST_BORROW         0 (__class__)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object __init__ at 0x1026e1b30, file "tasks/dictionary_lookup.py", line 11>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               STORE_NAME               4 (__init__)

  14           LOAD_CONST               2 (<code object get_combinations at 0x117f5c2a0, file "tasks/dictionary_lookup.py", line 14>)
               MAKE_FUNCTION
               STORE_NAME               5 (get_combinations)

  34           LOAD_CONST               3 (<code object get_nodes_features at 0x10249e810, file "tasks/dictionary_lookup.py", line 34>)
               MAKE_FUNCTION
               STORE_NAME               6 (get_nodes_features)

  52           LOAD_CONST               4 (<code object label at 0x1027ae1f0, file "tasks/dictionary_lookup.py", line 52>)
               MAKE_FUNCTION
               STORE_NAME               7 (label)

  56           LOAD_CONST               5 (<code object get_dims at 0x10253d920, file "tasks/dictionary_lookup.py", line 56>)
               MAKE_FUNCTION
               STORE_NAME               8 (get_dims)
               LOAD_CONST               6 (())
               STORE_NAME               9 (__static_attributes__)
               LOAD_FAST_BORROW         1 (__classdict__)
               STORE_NAME              10 (__classdictcell__)
               LOAD_FAST_BORROW         0 (__class__)
               COPY                     1
               STORE_NAME              11 (__classcell__)
               RETURN_VALUE

Disassembly of <code object __init__ at 0x1026e1b30, file "tasks/dictionary_lookup.py", line 11>:
  --           COPY_FREE_VARS           1

  11           RESUME                   0

  12           LOAD_GLOBAL              0 (super)
               LOAD_GLOBAL              2 (DictionaryLookupDataset)
               LOAD_FAST_BORROW         0 (self)
               LOAD_SUPER_ATTR         11 (__init__ + NULL|self)
               LOAD_FAST_BORROW         1 (depth)
               CALL                     1
               POP_TOP
               LOAD_CONST               0 (None)
               RETURN_VALUE

Disassembly of <code object get_combinations at 0x117f5c2a0, file "tasks/dictionary_lookup.py", line 14>:
  --           MAKE_CELL                6 (num_leaves)

  14           RESUME                   0

  17           LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                2 (leaf_indices)
               CALL                     1
               STORE_DEREF              6 (num_leaves)

  18           LOAD_CONST               0 (1000)
               STORE_FAST               1 (num_permutations)

  19           LOAD_CONST               1 (32000)
               STORE_FAST               2 (max_examples)

  21           LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                4 (depth)
               LOAD_SMALL_INT           3
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE      114 (to L5)
               NOT_TAKEN

  22           LOAD_GLOBAL              7 (min + NULL)
               LOAD_FAST_BORROW         1 (num_permutations)
               LOAD_GLOBAL              8 (math)
               LOAD_ATTR               10 (factorial)
               PUSH_NULL
               LOAD_DEREF               6 (num_leaves)
               CALL                     1
               LOAD_FAST_BORROW         2 (max_examples)
               LOAD_DEREF               6 (num_leaves)
               BINARY_OP                2 (//)
               CALL                     3
               STORE_FAST               3 (per_depth_num_permutations)

  24           LOAD_GLOBAL             13 (range + NULL)
               LOAD_FAST_BORROW         3 (per_depth_num_permutations)
               CALL                     1
               GET_ITER

  23           LOAD_FAST_AND_CLEAR      4 (_)
               SWAP                     2
       L1:     BUILD_LIST               0
               SWAP                     2

  24   L2:     FOR_ITER                51 (to L3)

  23           STORE_FAST               4 (_)
               LOAD_GLOBAL             14 (np)
               LOAD_ATTR               16 (random)
               LOAD_ATTR               19 (permutation + NULL|self)
               LOAD_GLOBAL             13 (range + NULL)
               LOAD_SMALL_INT           1
               LOAD_DEREF               6 (num_leaves)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               CALL                     2
               CALL                     1
               LIST_APPEND              2
               JUMP_BACKWARD           53 (to L2)

  24   L3:     END_FOR
               POP_ITER

  23   L4:     STORE_FAST               5 (permutations)
               STORE_FAST               4 (_)
               JUMP_FORWARD            99 (to L6)

  26   L5:     LOAD_GLOBAL             16 (random)
               LOAD_ATTR               20 (sample)
               PUSH_NULL
               LOAD_GLOBAL             23 (list + NULL)
               LOAD_GLOBAL             24 (itertools)
               LOAD_ATTR               26 (permutations)
               PUSH_NULL
               LOAD_GLOBAL             13 (range + NULL)
               LOAD_SMALL_INT           1
               LOAD_DEREF               6 (num_leaves)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               CALL                     2
               CALL                     1
               CALL                     1

  27           LOAD_GLOBAL              7 (min + NULL)
               LOAD_FAST_BORROW         1 (num_permutations)
               LOAD_GLOBAL              8 (math)
               LOAD_ATTR               10 (factorial)
               PUSH_NULL
               LOAD_DEREF               6 (num_leaves)
               CALL                     1
               CALL                     2

  26           CALL                     2
               STORE_FAST               5 (permutations)

  29   L6:     LOAD_GLOBAL             24 (itertools)
               LOAD_ATTR               28 (chain)
               LOAD_ATTR               31 (from_iterable + NULL|self)
               LOAD_FAST_BORROW         6 (num_leaves)
               BUILD_TUPLE              1
               LOAD_CONST               2 (<code object <genexpr> at 0x1024c3730, file "tasks/dictionary_lookup.py", line 29>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)

  32           LOAD_FAST_BORROW         5 (permutations)
               GET_ITER

  29           CALL                     0
               CALL                     1
               RETURN_VALUE

  --   L7:     SWAP                     2
               POP_TOP

  23           SWAP                     2
               STORE_FAST               4 (_)
               RERAISE                  0
ExceptionTable:
  L1 to L4 -> L7 [2]

Disassembly of <code object <genexpr> at 0x1024c3730, file "tasks/dictionary_lookup.py", line 29>:
  --           COPY_FREE_VARS           1

  29           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

  32   L2:     FOR_ITER                54 (to L3)
               STORE_FAST               1 (perm)

  31           LOAD_GLOBAL              1 (zip + NULL)
               LOAD_GLOBAL              3 (range + NULL)
               LOAD_SMALL_INT           1
               LOAD_DEREF               2 (num_leaves)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               CALL                     2
               LOAD_GLOBAL              4 (itertools)
               LOAD_ATTR                6 (repeat)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (perm)
               CALL                     1
               CALL                     2
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           56 (to L2)

  32   L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object get_nodes_features at 0x10249e810, file "tasks/dictionary_lookup.py", line 34>:
 34           RESUME                   0

 38           LOAD_FAST_BORROW         1 (combination)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   35 (selected_key, values)

 41           LOAD_FAST_BORROW         2 (selected_key)
              LOAD_SMALL_INT           0
              BUILD_TUPLE              2
              BUILD_LIST               1
              STORE_FAST               4 (nodes)

 43           LOAD_GLOBAL              1 (range + NULL)
              LOAD_SMALL_INT           1
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (num_nodes)
              CALL                     2
              GET_ITER
      L1:     FOR_ITER                83 (to L4)
              STORE_FAST               5 (i)

 44           LOAD_FAST_BORROW_LOAD_FAST_BORROW 80 (i, self)
              LOAD_ATTR                4 (leaf_indices)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       46 (to L2)
              NOT_TAKEN

 45           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                4 (leaf_indices)
              LOAD_ATTR                7 (index + NULL|self)
              LOAD_FAST_BORROW         5 (i)
              CALL                     1
              STORE_FAST               6 (leaf_num)

 46           LOAD_FAST_BORROW         6 (leaf_num)
              LOAD_SMALL_INT           1
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (values, leaf_num)
              BINARY_OP               26 ([])
              BUILD_TUPLE              2
              STORE_FAST               7 (node)
              JUMP_FORWARD             2 (to L3)

 48   L2:     LOAD_CONST               1 ((0, 0))
              STORE_FAST               7 (node)

 49   L3:     LOAD_FAST_BORROW         4 (nodes)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_FAST_BORROW         7 (node)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           85 (to L1)

 43   L4:     END_FOR
              POP_ITER

 50           LOAD_FAST_BORROW         4 (nodes)
              RETURN_VALUE

Disassembly of <code object label at 0x1027ae1f0, file "tasks/dictionary_lookup.py", line 52>:
 52           RESUME                   0

 53           LOAD_FAST_BORROW         1 (combination)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   35 (selected_key, values)

 54           LOAD_GLOBAL              1 (int + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (values, selected_key)
              LOAD_SMALL_INT           1
              BINARY_OP               10 (-)
              BINARY_OP               26 ([])
              CALL                     1
              LOAD_SMALL_INT           1
              BINARY_OP               10 (-)
              RETURN_VALUE

Disassembly of <code object get_dims at 0x10253d920, file "tasks/dictionary_lookup.py", line 56>:
 56           RESUME                   0

 58           LOAD_GLOBAL              1 (len + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (leaf_indices)
              CALL                     1
              STORE_FAST               1 (in_dim)

 59           LOAD_GLOBAL              1 (len + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (leaf_indices)
              CALL                     1
              STORE_FAST               2 (out_dim)

 60           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (in_dim, out_dim)
              BUILD_TUPLE              2
              RETURN_VALUE
'''

# Key constants:
#   0: 0
#   1: None
#   4: 'DictionaryLookupDataset'

# Names used:
#   0: numpy
#   1: np
#   2: itertools
#   3: random
#   4: math
#   5: tasks.tree_dataset
#   6: TreeDataset
#   7: common
#   8: DictionaryLookupDataset
