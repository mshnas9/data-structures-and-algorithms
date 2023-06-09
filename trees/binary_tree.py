class Node:
    def __init__(self, value):
        """Initialize a Node object with a given value."""
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self, root):
        """Initialize a BinaryTree object with a given root."""
        self.root = root

    def pre_order(self, root):
        """Traverse the tree in pre-order and return a list of node values."""
        if root is None:
            raise ValueError("Tree is empty")
        arr = []
        arr.append(root.value)

        if root.left:
            arr += self.pre_order(root.left)
        if root.right:
            arr += self.pre_order(root.right)
        return arr

    def in_order(self, root):
        """Traverse the tree in in-order and return a list of node values."""
        if root is None:
            raise ValueError("Tree is empty")
        arr = []
        if root.left:
            arr += self.in_order(root.left)

        if root:
            arr.append(root.value)

        if root.right:
            arr += self.in_order(root.right)
        return arr

    def post_order(self, root):
        """Traverse the tree in post-order and return a list of node values."""
        if root is None:
            raise ValueError("Tree is empty")
        arr = []
        if root.left:
            arr += self.post_order(root.left)
        if root.right:
            arr += self.post_order(root.right)
        if root:
            arr.append(root.value)
        return arr


    def find_maximum_value(self):
        """Function to find the maximum value in a binary tree."""
        if self.root is None:
            raise ValueError("Empty tree")

        max_value = self.root.value

        def _walk(node):
            nonlocal max_value

            if node.value > max_value:
                max_value = node.value

            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)

        _walk(self.root)

        return max_value
    
    def  breadth_first(self):
        """Function to traverse a tree using breadth first approach."""
        if self.root is None:
            raise ValueError("Empty tree")
        arr = []
        arr.append(self.root)
        for i in arr:
            if i.left:
                arr.append(i.left)
            if i.right:
                arr.append(i.right)
        return [i.value for i in arr]


class BinarySearchTree(BinaryTree):
    def add(self, value):
        """Add a new node with the given value to the binary search tree."""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right
            else:
                return

    def contains(self, value):
        """Check if the binary search tree contains a node with the given value."""
        if self.root is None:
            return False

        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True

        return False
