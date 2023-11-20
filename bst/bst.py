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

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest
            # in the right subtree)
            root.key = self._min_value_node(root.right).key

            # Delete the inorder successor
            root.right = self._delete(root.right, root.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def height(self):
        return self._height(self.root)

    def _height(self, root):
        if root is None:
            return 0
        else:
            left_height = self._height(root.left)
            right_height = self._height(root.right)
            return max(left_height, right_height) + 1

    def display_in_order(self):
        elements = []
        self._in_order_traversal(self.root, elements)
        print("In-order Traversal:", elements)

    def _in_order_traversal(self, root, elements):
        if root:
            self._in_order_traversal(root.left, elements)
            elements.append(root.key)
            self._in_order_traversal(root.right, elements)


# Example usage:
bst = BinarySearchTree()
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    bst.insert(key)

print("Original BST:")
bst.display_in_order()
print("Height:", bst.height())

bst.delete(30)

print("\nBST after deleting node with key 30:")
bst.display_in_order()
print("Height:", bst.height())
