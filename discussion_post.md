# Unit 4 Discussion: Employee-ID Binary Search Tree

**Author: Firaz Khan**

Repository: https://github.com/fkumgc/CMSC315_wk4

I implemented an employee-ID index using a binary search tree (BST). Each node stored one unique ID and references to at most two children. Recursive insertion placed smaller IDs in the left subtree and larger IDs in the right subtree, while duplicate IDs were ignored. In-order traversal visited left, current, then right, producing a sorted list for an employee directory (Vashishtha, 2025).

I learned how recursive base cases connected insertion, searching, and traversal. One implementation challenge was preserving child references when recursive insertion returned a new node. I addressed this by assigning each returned subtree to its parent's left or right reference. I also tested empty trees, single nodes, missing IDs, duplicates, and invalid inputs.

My demonstration inserted the same 15 IDs in two orders. Searching for the largest ID visited four nodes in the balanced example and 15 in the sequential example. Balanced BST searches took O(log n), compared with O(n) linear searches. However, sorted insertion produced a chain and reduced search efficiency to O(n), illustrating the importance of tree height (Mateen, 2025). A sorted array also supported O(log n) binary search, but insertion could require shifting elements. An AVL tree would help preserve efficiency as employee records grew.

## References

Mateen, A. (2025, April 8). *Binary search tree—An efficient data structure*. Medium. https://medium.com/@amateen_74225/binary-search-tree-an-efficient-data-structure-36cb7b7a2d4b

Vashishtha, A. (2025, July 31). *Binary search trees (BST): A complete learning guide*. Medium. https://medium.com/@anandvashishtha/binary-search-trees-bst-a-complete-learning-guide-c97aa49ebc28
