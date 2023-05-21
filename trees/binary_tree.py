# binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """Class to create a binary tree"""

    def __init__(self, value=None):
        self.root = None

    def pre_order(self, node=None, array_tree=None):
        """Recursive function to perform preorder traversal on the tree
           root >> left >> right
        """

        if self.root is None:
            raise ValueError("Empty tree")

        if array_tree is None:
            array_tree = []

        node = node or self.root

        # Display the data part of the root node
        array_tree.append(node.value)

        # Traverse the left subtree
        if node.left:
            self.pre_order(node.left, array_tree)

        # Traverse the right subtree
        if node.right:
            self.pre_order(node.right, array_tree)

        return array_tree

    def in_order(self, node=None, array_tree=None):
        """Recursive function to perform inorder traversal on the tree
           left >> root >> right
        """
        if self.root is None:
            raise ValueError("Empty tree")

        if array_tree is None:
            array_tree = []

        node = node or self.root

        if node.left:
            self.in_order(node.left, array_tree)

        array_tree.append(node.value)

        if node.right:
            self.in_order(node.right, array_tree)

        return array_tree

    def post_order(self, node=None, array_tree=None):
        """Recursive function to perform postorder traversal on the tree
              left >> right >> root
        """

        if self.root is None:
            raise ValueError("Empty tree")

        if array_tree is None:
            array_tree = []

        node = node or self.root

        if node.left:
            self.post_order(node.left, array_tree)

        if node.right:
            self.post_order(node.right, array_tree)

        array_tree.append(node.value)

        return array_tree


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self, value):
        """Add a new node with the given value in the correct location in the binary search tree."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def contains(self, value):
        """Check if the value is present in the binary search tree."""
        node = self.root

        while node is not None:
            if node.value == value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right

        return False
