import pytest
from insert_sort import InsertionSort, Insert

def test_insert():
    sorted = [1, 2, 3, 4, 5]
    value = 3
    Insert(sorted, value)
    assert sorted == [1, 2, 3, 3, 4, 5]

def test_insertion_sort():
    input = [5, 4, 3, 2, 1]
    sorted = InsertionSort(input)
    assert sorted == [1, 2, 3, 4, 5]