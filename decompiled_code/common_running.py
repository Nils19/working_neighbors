# Reconstructed from: __pycache__/common.cpython-314.pyc
# What's actually running in PID 72504
# Bytecode disassembly:

"""
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
              LOAD_CONST               6 (<code object Task at 0x1033d2670, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 10>)
              MAKE_FUNCTION
              LOAD_CONST               7 ('Task')
              LOAD_NAME                1 (Enum)
              CALL                     3
              STORE_NAME              14 (Task)

 29           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST               8 (<code object GNN_TYPE at 0x1031ca970, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 29>)
              MAKE_FUNCTION
              LOAD_CONST               9 ('GNN_TYPE')
              LOAD_NAME                1 (Enum)
              CALL                     3
              STORE_NAME              15 (GNN_TYPE)

 59           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST              10 (<code object STOP at 0x1033d21f0, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 59>)
              MAKE_FUNCTION
              LOAD_CONST              11 ('STOP')
              LOAD_NAME                1 (Enum)
              CALL                     3
              STORE_NAME              16 (STOP)

 71           LOAD_CONST              12 (<code object one_hot at 0x10321cc10, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 71>)
              MAKE_FUNCTION
              STORE_NAME              17 (one_hot)
              LOAD_CONST              13 (None)
              RETURN_VALUE

Disassembly of <code object Task at 0x1033d2670, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 10>:
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

  14           LOAD_CONST               1 (<code object from_string at 0x1033d2430, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 13>)
               MAKE_FUNCTION

  13           CALL                     0

  14           STORE_NAME               7 (from_string)

  20           LOAD_CONST               2 (<code object get_dataset at 0x1031cb730, file "/Users/nilscollins/Documents/TUM/bottleneck/common.py", line 20>)
               MAKE_FUNCTION
               STORE_NAME               8 (get_dataset)
               LOAD_CONST               3 (())
       
... (truncated)
"""

