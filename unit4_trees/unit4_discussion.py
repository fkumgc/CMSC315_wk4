"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


# Author: Firaz Khan
# Application: an index of unique employee IDs.


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        self._validate_id(value)
        # Save the returned root so insertion also works for an empty tree.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None:
            return Node(value)
        # Every value in the left subtree must be smaller than this node;
        # every value in the right subtree must be larger.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Equal IDs represent the same employee, so duplicates are ignored.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        self._validate_id(value)
        # Ordering rules out the other subtree at each comparison. This is
        # O(h), or O(log n) when balanced, but O(n) in a skewed tree.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return
        # Left values are smaller; right values are larger. Applying this
        # rule recursively visits every unique ID in ascending order.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)

    @staticmethod
    def _validate_id(value):
        # Employee IDs must be positive integers; bool is excluded even
        # though Python treats bool as a subclass of int.
        if type(value) is not int:
            raise TypeError("Employee ID must be an integer (not a boolean).")
        if value <= 0:
            raise ValueError("Employee ID must be positive.")


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    # TODO: Create a BST and insert multiple values.
    tree = BST()
    employee_ids = [1050, 1025, 1075, 1010, 1035, 1060, 1090,
                    1001, 1015, 1030, 1040, 1055, 1065, 1080, 1095]
    for employee_id in employee_ids:
        tree.insert(employee_id)
    print("Employee IDs inserted:", employee_ids)
    # This middle-first order creates short paths; the BST does not rebalance.
    print("Smaller IDs went left; larger IDs went right from each node.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    # TODO: Display and explain traversal results.
    print("Employee IDs in ascending order:", tree.inorder())
    # Left-root-right visits smaller IDs before the current ID, then larger IDs.
    print("Left -> current -> right produced a sorted employee-ID report.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # TODO: Demonstrate BST searching.
    # Root, internal, minimum, and maximum IDs exist; the gap and outside IDs do not.
    for employee_id in [1050, 1025, 1001, 1095, 1042, 999, 1100]:
        print(f"Search {employee_id}: {'Found' if tree.search(employee_id) else 'Not found'}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    # TODO: Demonstrate and explain an edge case.
    empty = BST()
    print("Empty traversal:", empty.inorder(), "(expected [])")
    print("Empty search:", empty.search(1050), "(expected False)")
    single = BST()
    single.insert(1050)
    print("Single-node tree:", single.inorder(), "Found:", single.search(1050))
    # Duplicate insertion leaves the unique employee index unchanged.
    before = tree.inorder()
    tree.insert(1050)
    print("Duplicate 1050 ignored:", tree.inorder() == before)
    # Invalid operations fail before they can modify the tree.
    for invalid in ["1050", None, True, 1050.5, 0, -1]:
        for operation in (tree.insert, tree.search):
            try:
                operation(invalid)
            except (TypeError, ValueError) as error:
                print(f"{operation.__name__}({invalid!r}) rejected: {error}")

    print("\n=== INSERTION ORDER AND PERFORMANCE ===")
    skewed = BST()
    for employee_id in sorted(employee_ids):
        skewed.insert(employee_id)
    # Identical values give identical sorted output, but different search paths.
    print("Same sorted IDs:", tree.inorder() == skewed.inorder())
    for label, example in [("Middle-first", tree), ("Sequential", skewed)]:
        node = example.root
        comparisons = 0
        target_id = max(employee_ids)
        while node is not None:
            comparisons += 1
            if target_id == node.value:
                break
            node = node.left if target_id < node.value else node.right
        print(f"{label}: search {target_id} visited {comparisons} nodes.")
    print("Balanced paths took 4 comparisons; sequential insertion took 15.")



if __name__ == "__main__":
    main()