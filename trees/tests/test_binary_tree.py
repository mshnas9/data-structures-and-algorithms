import pytest
from binary_tree import BinaryTree

# Raise value error if empty tree
def test_empty_tree():
    
    tree = BinaryTree()
    with pytest.raises(ValueError):
        tree.pre_order()