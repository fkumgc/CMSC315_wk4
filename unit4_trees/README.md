# Unit 4 Discussion: Binary Search Trees

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

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Completed Implementation

**Author: Firaz Khan**

I completed all 12 `TODO (Student)` blocks and retained the starter's comments and prompts. I converted the four TODO output placeholders to comments and replaced their output with completed demonstrations. I modeled a unique employee-ID index; the nodes stored IDs, rather than full employee records. A complete personnel application could associate each ID with a record.

I initialized each node with a value and two empty child references. I initialized the tree with an empty root. Recursive insertion returned a new node at an empty position, followed the smaller-left/larger-right rule, and reassigned the returned child reference. Equal IDs left the existing tree unchanged. Recursive search returned `False` at an empty position, returned `True` on equality, and otherwise followed only the possible subtree. In-order traversal collected left-subtree IDs, the current ID, and right-subtree IDs into a fresh list, which produced ascending order.

I inserted 15 IDs into both subtrees. I tested four existing IDs and three missing IDs, including a gap and values beyond the dataset boundaries. I demonstrated empty traversal (`[]`), empty search (`False`), a single node, and ignored duplicates. I required positive integer IDs; invalid types raised `TypeError`, while zero and negative IDs raised `ValueError`. I rejected booleans explicitly because Python treated them as integers. Invalid operations left the tree unchanged.

## Performance and Limitations

I compared two insertion orders for the same 15 IDs. The middle-first order created a tree with four levels, while sequential insertion created a 15-level right chain. Searching for 1095 visited four nodes in the first tree and 15 in the second. Both traversals returned the same sorted IDs, which showed that sorted output alone did not prove that a tree was balanced.

I analyzed insertion and search as O(h), where h represented tree height: O(log n) for a balanced tree and O(n) for a chain. Each comparison eliminated an entire subtree, but it did not necessarily eliminate half the remaining nodes. Traversal visited every node in O(n) time and returned O(n) output. Recursive calls used O(h) stack space. Building a tree from sorted input required O(n²) total insertion time. My implementation did not rebalance itself; sufficiently deep inputs could exceed Python's recursion limit. An AVL or red-black tree would address height growth, while iterative operations would avoid recursion depth failures without correcting a poor tree shape.

I compared the BST with an unsorted list, which required O(n) searches, and a sorted array, which supported O(log n) binary search but could require O(n) insertion shifts. A hash table supported expected O(1) lookup but did not maintain keys in sorted order automatically. The BST combined ordered output with dynamic insertion, subject to its height limitation. I used a small dataset to demonstrate the recursive design required by the assignment.

## Execution and Verification

I ran the original starter and observed only its TODO headings and messages. I then ran the completed program with Python 3 and verified the results saved in `sample_output.txt`. I ran five automated test methods covering empty and singleton trees, duplicates, ascending/descending/shuffled insertions, all inserted keys, missing keys, subtree ordering, positive-ID boundaries, invalid operations, and independence of the returned traversal list. All five tests passed.

Commands used from the repository root:

```text
python unit4_trees/unit4_discussion.py
python -m unittest discover -s unit4_trees -v
```

The validation used a bundled Python interpreter because `python` was not on the shell PATH. IntelliJ and its Python Plugin were not verified through the available tools. The course `submission_checklist.md` was located in the week 1 discussion project and was copied to the repository root because the supplied week 4 folder did not contain one.

## Reflection Essay (150–200 Words)

I implemented an employee-ID index using a binary search tree (BST). Each node stored one unique ID and references to at most two children. Recursive insertion placed smaller IDs in the left subtree and larger IDs in the right subtree, while duplicate IDs were ignored. In-order traversal visited left, current, then right, producing a sorted list for an employee directory (Vashishtha, 2025).

I learned how recursive base cases connected insertion, searching, and traversal. One implementation challenge was preserving child references when recursive insertion returned a new node. I addressed this by assigning each returned subtree to its parent's left or right reference. I also tested empty trees, single nodes, missing IDs, duplicates, and invalid inputs.

My demonstration inserted the same 15 IDs in two orders. Searching for the largest ID visited four nodes in the balanced example and 15 in the sequential example. Balanced BST searches took O(log n), compared with O(n) linear searches. However, sorted insertion produced a chain and reduced search efficiency to O(n), illustrating the importance of tree height (Mateen, 2025). A sorted array also supported O(log n) binary search, but insertion could require shifting elements. An AVL tree would help preserve efficiency as employee records grew.

## References

Mateen, A. (2025, April 8). *Binary search tree—An efficient data structure*. Medium. https://medium.com/@amateen_74225/binary-search-tree-an-efficient-data-structure-36cb7b7a2d4b

Vashishtha, A. (2025, July 31). *Binary search trees (BST): A complete learning guide*. Medium. https://medium.com/@anandvashishtha/binary-search-trees-bst-a-complete-learning-guide-c97aa49ebc28
