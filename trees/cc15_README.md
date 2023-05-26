# Trees 
<!-- Description of the challenge -->
This project implements a Binary Search Tree data structure in Python. It consists of three main classes: **`Node`**, **`BinaryTree`**, and **`BinarySearchTree`**. The **`Node`** class represents a single node in the tree, storing the node's value, left child node, and right child node. The **`BinaryTree`** class provides methods for depth-first traversals of the tree, including pre-order, in-order, and post-order traversals. The **`BinarySearchTree`** class is a sub-class of **`BinaryTree`** and includes additional methods specific to binary search trees.

### **Features**

### Node

- Represents a node in the binary search tree.
- Properties include the value stored in the node, the left child node, and the right child node.

### Binary Tree

- Represents a binary tree.
- Includes methods for depth-first traversals:
    - Pre-order traversal
    - In-order traversal
    - Post-order traversal
- Each traversal method returns an array of values, ordered accordingly.

### Binary Search Tree

- Represents a binary search tree, a subclass of the **`BinaryTree`** class.
- Additional methods include:
    - Add: Adds a new node with the given value to the correct location in the binary search tree.
    - Contains: Checks if the given value exists in the tree at least once and returns a boolean indicating the result.## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Adding a new node to the binary search tree follows a recursive approach. Starting from the root, the value is compared with the current node, and based on the comparison, the traversal continues to the left or right subtree until an appropriate empty spot is found to insert the new node. The time complexity for the **`add`** operation is O(log N) on average, where N is the number of nodes in the tree. However, in the worst case scenario where the tree is highly unbalanced, the time complexity can degrade to O(N).
- Searching for a value in the binary search tree also follows a recursive approach. Starting from the root, the value is compared with the current node, and based on the comparison, the traversal continues to the left or right subtree until the value is found or until a leaf node is reached. The time complexity for the **`contains`** operation is O(log N) on average, and in the worst case scenario, it can be O(N) for an unbalanced tree.
- The depth-first traversals (pre-order, in-order, and post-order) visit every node in the tree once. Hence, the time complexity for these operations is O(N), where N is the number of nodes in the tree. The space complexity for the traversals is also O(N) due to the usage of the call stack for recursive function calls.

## Solution
<!-- Show how to run your code, and examples of it in action -->
```Python
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
```