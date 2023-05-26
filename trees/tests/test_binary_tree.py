import pytest
from binary_tree import BinaryTree, Node, BinarySearchTree
tree1 = BinaryTree(Node("A"))

node2 = Node("B")
tree1.root.left = node2

node3 = Node("C")
tree1.root.right = node3

node4 = Node("D")
tree1.root.left.left = node4

node5 = Node("E")
tree1.root.left.right = node5

node6 = Node("F")
tree1.root.right.left = node6

# Can successfully instantiate an empty tree


def test_empty_tree():
    tree = BinaryTree(root=None)
    with pytest.raises(ValueError):
        tree.pre_order(tree.root)

# Can successfully instantiate a tree with a single root node


def test_single_root_node():
    tree = BinaryTree(Node("A"))
    expected = 'A'
    actual = tree.root.value
    assert expected == actual

# Can successfully return a collection from a pre-order traversal


def test_pre_order():
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    actual = tree1.pre_order(tree1.root)
    assert expected == actual

# Can successfully return a collection from a in-order traversal

def test_in_order():
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    actual = tree1.in_order(tree1.root)
    assert expected == actual

# Can successfully return a collection from a post-order traversal

def test_post_order():
    expected = ['D','E','B','F','C','A']
    actual = tree1.post_order(tree1.root)
    assert expected == actual


def test_add_node():
    tree = BinarySearchTree(Node(5))
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)
    expected = [5, 3, 2, 4, 7, 6, 8]
    actual = tree.pre_order(tree.root)
    assert expected == actual

def test_contains():
    tree = BinarySearchTree(Node(5))
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)
    expected = True
    actual = tree.contains(4)
    assert expected == actual
