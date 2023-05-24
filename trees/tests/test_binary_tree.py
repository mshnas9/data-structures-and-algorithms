import pytest
from binary_tree import BinaryTree,Node

# Can successfully instantiate an empty tree
def test_empty_tree():
    tree = BinaryTree()
    assert tree.root is None
# Can successfully instantiate a tree with a single root node
def test_single_root():
    tree = BinaryTree(1)
    assert tree.root.data == 1
# Can successfully add a left child and right child to a single root node
# def test_add_children():
#     tree = BinaryTree(1)
#     tree.root.left = 2
#     tree.root.right = 3
#     assert tree.root.left.data == 2
#     assert tree.root.right.data == 3
def test_add_children():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    assert tree.root.left.data == 2
