class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """Class to create a binary tree"""

    def __init__(self, value=None):
        if value is not None:
            self.root = Node(value)
        else:
            self.root = None

    def pre_order(self, node=None, array_tree=None):
        """Perform preorder traversal on the tree."""
        if self.root is None:
            raise ValueError("Empty tree")

        if array_tree is None:
            array_tree = []

        node = node or self.root

        array_tree.append(node.value)

        if node.left:
            self.pre_order(node.left, array_tree)

        if node.right:
            self.pre_order(node.right, array_tree)

        return array_tree

    def in_order(self, node=None, array_tree=None):
        """Perform inorder traversal on the tree."""
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
        """Perform postorder traversal on the tree."""
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
            return

        node = self.root

        while True:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    return
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    return
                else:
                    node = node.right

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
