import pytest
from merge import merge_sort

def test_merge_sort():
    arr = [1, 10, 9, 5]
    expected = [1, 5, 9, 10]
    actual = merge_sort(arr)
    assert expected == actual

def test_merge_sort_empty():
    arr = []
    expected = None
    actual = merge_sort(arr)
    assert expected == actual

def test_merge_sort_sorted():
    arr = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    actual = merge_sort(arr)
    assert expected == actual

def test_merge_sort_reversed():
    arr = [4, 3, 2, 1]
    expected = [1, 2, 3, 4]
    actual = merge_sort(arr)
    assert expected == actual