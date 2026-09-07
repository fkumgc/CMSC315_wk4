"""Behavior and ordering checks for Firaz Khan's employee-ID BST."""

import random
import unittest

from unit4_discussion import BST


class BSTTests(unittest.TestCase):
    def assert_ordered(self, node, lower=0, upper=float('inf')):
        if node is None:
            return
        self.assertLess(lower, node.value)
        self.assertLess(node.value, upper)
        self.assert_ordered(node.left, lower, node.value)
        self.assert_ordered(node.right, node.value, upper)

    def test_empty(self):
        tree = BST()
        self.assertEqual(tree.inorder(), [])
        self.assertFalse(tree.search(1001))

    def test_single_and_duplicate(self):
        tree = BST()
        tree.insert(1001)
        tree.insert(1001)
        self.assertEqual(tree.inorder(), [1001])
        self.assertTrue(tree.search(1001))
        self.assertFalse(tree.search(1002))

    def test_insertion_orders_and_search(self):
        values = list(range(1001, 1101))
        shuffled = values.copy()
        random.Random(315).shuffle(shuffled)
        for order in (values, values[::-1], shuffled):
            with self.subTest(first=order[0]):
                tree = BST()
                for value in order:
                    tree.insert(value)
                tree.insert(order[-1])
                self.assertEqual(tree.inorder(), values)
                self.assert_ordered(tree.root)
                for value in values:
                    self.assertTrue(tree.search(value))
                self.assertFalse(tree.search(1000))
                self.assertFalse(tree.search(1101))

    def test_invalid_operations_preserve_tree(self):
        for seeded in (False, True):
            tree = BST()
            if seeded:
                tree.insert(1050)
            before = tree.inorder()
            for invalid in ('1050', None, True, False, 1.5, [], 0, -1):
                error = ValueError if type(invalid) is int else TypeError
                for operation in (tree.insert, tree.search):
                    with self.subTest(value=invalid, method=operation.__name__):
                        with self.assertRaises(error):
                            operation(invalid)
                        self.assertEqual(tree.inorder(), before)

    def test_boundaries_gap_and_result_independence(self):
        tree = BST()
        for value in (1050, 1, 10**20):
            tree.insert(value)
        self.assertTrue(tree.search(1))
        self.assertTrue(tree.search(10**20))
        self.assertFalse(tree.search(1049))
        result = tree.inorder()
        result.clear()
        self.assertEqual(tree.inorder(), [1, 1050, 10**20])


if __name__ == '__main__':
    unittest.main()
