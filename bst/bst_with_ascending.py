"""
Algorithm InsertElementsInAscendingOrder(BST, elements):
    Input: BST - Binary Search Tree
            elements - List of elements in ascending order

    1. Initialize an empty BST.
    2. For each element in the 'elements' list:
        a. Insert the element into the BST.

    Output: BST with elements inserted in ascending order.
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.key:
                root.left = self._insert(root.left, key)
            else:
                root.right = self._insert(root.right, key)
        return root

    def display_in_order(self):
        elements = []
        self._in_order_traversal(self.root, elements)
        print("In-order Traversal:", elements)

    def _in_order_traversal(self, root, elements):
        if root:
            self._in_order_traversal(root.left, elements)
            elements.append(root.key)
            self._in_order_traversal(root.right, elements)


def insert_elements_in_ascending_order(bst, elements):
    for element in elements:
        bst.insert(element)


# Example usage
ascending_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]

bst = BinarySearchTree()

insert_elements_in_ascending_order(bst, ascending_elements)

print("BST with elements in ascending order:")
bst.display_in_order()

