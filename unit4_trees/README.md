# Unit 4: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Implementation Summary

**Author: Firaz Khan**

The BST was implemented with a `Node` class that stored a unique employee ID and
left and right child references. All 12 TODO blocks were completed, and the
original comments and prompts were preserved. Recursive insertion created a node
at an empty position, placed smaller IDs to the left and larger IDs to the right,
and returned the updated node reference. Duplicate IDs left the tree unchanged.

Recursive search returned `True` when an ID matched and `False` when an empty
position was reached. Each comparison eliminated the subtree that could not
contain the target. In-order traversal visited the left subtree, current node,
and right subtree, producing ascending IDs because the same ordering rule held
throughout the tree.

Insertion and search required O(h) time: O(log n) for a balanced tree and O(n)
for a chain. Traversal required O(n) time and O(n) output space, while recursion
used O(h) stack space. The implementation did not rebalance itself. Sorted
insertion required O(n²) total construction time, and sufficiently deep trees
could exceed Python's recursion limit. An AVL tree would help maintain short
paths; iterative operations would avoid recursion depth failures.

## Program Output and Testing

The starter was run and displayed only TODO messages. The completed program
inserted 15 IDs and produced a sorted traversal. Searches found four existing
IDs and correctly rejected three missing IDs, including a gap and values beyond
the dataset boundaries. Empty traversal returned `[]`, empty search returned
`False`, and single-node and duplicate cases behaved as expected.

Positive integer IDs were required. Strings, `None`, floats, and booleans raised
`TypeError`; zero and negative values raised `ValueError`. Invalid operations
left the tree unchanged. Five automated test methods passed, including checks
for ascending, descending, and shuffled insertion orders and subtree ordering.
Tests and captured output were retained separately from the submission files.

The same 15 IDs were inserted in middle-first and sequential orders. Searching
for 1095 visited four nodes in the first tree and 15 in the second. Both trees
produced identical sorted output, showing that sorted traversal alone did not
establish that a tree was balanced.

The program was executed with Python 3. The equivalent command from this folder was:

```text
python unit4_discussion.py
```

## Real-World Interpretation

The application modeled an employee-ID index that supported membership checks
and ordered reporting. Nodes stored IDs; a personnel system could associate
each ID with a full record. An unsorted list required O(n) searches. A sorted
array supported O(log n) binary search but could require O(n) insertion shifts.
A hash table supported expected O(1) lookup without automatically maintaining
sorted keys. The BST combined dynamic insertion and ordered output, with
performance determined by its shape.
