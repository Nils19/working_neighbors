# Reconstructed from: tasks/__pycache__/dictionary_lookup.cpython-314.pyc
# What's actually running in PID 72504
# Bytecode disassembly:

"""
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
              LOAD_CONST               3 (<code object DictionaryLookupDataset at 0x1033d2310, file "tasks/dictionary_lookup.py", line 10>)
              MAKE_FUNCTION
              LOAD_CONST               4 ('DictionaryLookupDataset')
              LOAD_NAME                6 (TreeDataset)
              CALL                     3
              STORE_NAME               8 (DictionaryLookupDataset)
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object DictionaryLookupDataset at 0x1033d2310, file "tasks/dictionary_lookup.py", line 10>:
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
               LOAD_CONST               1 (<code object __init__ at 0x1031a5b30, file "tasks/dictionary_lookup.py", line 11>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               STORE_NAME               4 (__init__)

  14           LOAD_CONST               2 (<code object get_combinations at 0x112035a10, file "tasks/dictionary_lookup.py", line 14>)
               MAKE_FUNCTION
               STORE_NAME               5 (get_combinations)

  34           LOAD_CONST               3 (<code object get_nodes_features at 0x10306e810, file "tasks/dictionary_lookup.py", line 34>)
               MAKE_FUNCTION
               STORE_NAME               6 (get_nodes_features)

  52           LOAD_CONST               4 (<code object label at 0x1033d21f0, file "tasks/dictionary_lookup.py", line 52>)
               MAKE_FUNCTION
               STORE_NAME               7 (label)

  56           LOAD_CONST               5 (<code object get_dims at 0x10321cc10, file "tasks/dictionary_lookup.py", line 56>)
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

Disassembly of <code object __init__ at 0x1031a5b30, file "tasks/dictionary_lookup.py", line 11>:
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

Disassembly of <code object get_combinations at 0x112035a10, file "tasks/dictionary_lookup.py", line 14>:
  --           MAKE_CELL                6 (num_leaves)

  14           RESUME                   0

  17           LOAD_GLOBAL              1
... (truncated)
"""

