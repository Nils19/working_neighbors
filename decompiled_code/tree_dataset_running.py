# Reconstructed from: tasks/__pycache__/tree_dataset.cpython-314.pyc
# What's actually running in PID 72504
# Bytecode disassembly:

"""
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
              LOAD_CONST               5 (<code object TreeDataset at 0x1031ca970, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 9>)
              MAKE_FUNCTION
              LOAD_CONST               6 ('TreeDataset')
              LOAD_NAME                9 (object)
              CALL                     3
              STORE_NAME              10 (TreeDataset)
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object TreeDataset at 0x1031ca970, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 9>:
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
               LOAD_CONST               1 (<code object __init__ at 0x1030d77b0, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 10>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               STORE_NAME               4 (__init__)

  16           LOAD_CONST               2 (<code object add_child_edges at 0x11202f0a0, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 16>)
               MAKE_FUNCTION
               STORE_NAME               5 (add_child_edges)

  33           LOAD_CONST               3 (<code object _create_blank_tree at 0x103093730, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 33>)
               MAKE_FUNCTION
               STORE_NAME               6 (_create_blank_tree)

  38           LOAD_CONST              11 ((True,))
               LOAD_CONST               4 (<code object create_blank_tree at 0x1030de970, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 38>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME               7 (create_blank_tree)

  47           LOAD_CONST               5 (<code object generate_data at 0x112035f40, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 47>)
               MAKE_FUNCTION
               STORE_NAME               8 (generate_data)

  71           LOAD_CONST               6 (<code object get_combinations at 0x1033c16f0, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 71>)
               MAKE_FUNCTION
               STORE_NAME               9 (get_combinations)

  74           LOAD_CONST               7 (<code object get_nodes_features at 0x1033c25d0, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 74>)
               MAKE_FUNCTION
               STORE_NAME              10 (get_nodes_features)

  77           LOAD_CONST               8 (<code object label at 0x1033c2870, file "/Users/nilscollins/Documents/TUM/bottleneck/tasks/tree_dataset.py", line 77>)
               MAKE_FUNCTION
               STORE_NAME              11 (label)

  80           LOAD_CONST               9 (<code object get_dims at 0x1033c2790, file "/Users/nilscollins/Documents/TUM/bottleneck/ta
... (truncated)
"""

