import pytest
from linkedlist import LinkedList


#test Can successfully instantiate an empty linked list
def test_empty_linked_list():
    excepted = None
    actual = LinkedList().head
    assert excepted == actual
#test Can properly insert into the linked list
def test_insert():
    expected = 1
    linked_list = LinkedList()
    linked_list.insert(1)
    actual = linked_list.head.value
    assert expected == actual
#test The head property will properly point to the first node in the linked list
def test_head():
    expected = 2
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    actual = linked_list.head.value
    assert expected == actual
# test Can properly insert multiple nodes into the linked list
def test_insert_multiple_nodes():
    expected = '{ 3 } -> { 2 } -> { 1 } -> NULL'
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    actual = linked_list.__str__()
    assert expected == actual
# test Will return true when finding a value within the linked list that exists
def test_includes():
    expected = True
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    actual = linked_list.includes(2)
    assert expected == actual
# test Will return false when searching for a value in the linked list that does not exist
def test_not_includes():
    expected = False
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    actual = linked_list.includes(4)
    assert expected == actual
# test Can properly return a collection of all the values that exist in the linked list
def test_return_collection():
    expected = '{ 3 } -> { 2 } -> { 1 } -> NULL'
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    actual = linked_list.__str__()
    assert expected == actual

def test_append():
    excepted = 3
    ll = LinkedList()
    ll.append(3)
    actual = ll.head.value
    assert excepted == actual

def test_multiple_append():
    excepted = '{ 1 } -> { 2 } -> { 3 } -> NULL'
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.__str__()
    assert excepted == actual

def test_insert_before():
    excepted = '{ 1 } -> { 2 } -> { 11 } -> { 3 } -> NULL'
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(3,11)
    actual = ll.__str__()
    assert excepted == actual

def test_insert_before_first_value():
    excepted = '{ 11 } -> { 1 } -> { 2 } -> { 3 } -> NULL'
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(1,11)
    actual = ll.__str__()

def test_insert_after():
    excepted = '{ 1 } -> { 2 } -> { 11 } -> { 3 } -> NULL'
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(2,11)
    actual = ll.__str__()
    assert excepted == actual

def test_insert_after_last_value():
    excepted = '{ 1 } -> { 2 } -> { 3 } -> { 11 } -> NULL'
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(3,11)
    actual = ll.__str__()
    assert excepted == actual
 

# def test_kof2():
#     excepted = 3
#     ll = LinkedList()
#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     ll.append(7)
#     ll.append(9)
#     actual = ll.kth_from_end(2)
#     assert excepted == actual


# def test_kth_from_end_when_k_is_greater_than_length():
#     # Create a linked list [1, 2, 3, 4, 5]
#     ll = LinkedList()
#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     ll.append(4)
#     ll.append(5)

#     # Test when k is greater than the length of the linked list
#     assert ll.kth_from_end(6) is None


# def test_kth_from_end_when_k_and_length_are_same():
#     # Create a linked list [1, 2, 3, 4, 5]
#     ll = LinkedList()
#     excepted = None
#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     ll.append(4)
#     ll.append(5)

#     # Test when k and the length of the list are the same
#     assert ll.kth_from_end(5) == excepted


# def test_kth_from_end_when_k_is_not_positive():
#     # Create a linked list [1, 2, 3, 4, 5]
#     ll = LinkedList()
#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     ll.append(4)
#     ll.append(5)

#     # Test when k is not a positive integer
#     assert ll.kth_from_end(-1) is None


# def test_kth_from_end_when_linked_list_is_of_size_1():
#     # Create a linked list with a single element
#     ll_single = LinkedList()
#     ll_single.append(1)

#     # Test when the linked list is of size 1
#     assert ll_single.kth_from_end(0) == 1


# def test_kth_from_end_happy_path():
#     # Create a linked list [1, 2, 3, 4, 5]
#     ll = LinkedList()
#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     ll.append(4)
#     ll.append(5)

#     # Test the "Happy Path" scenario where k is in the middle of the linked list
#     assert ll.kth_from_end(2) == 3

def test_kth_from_end_when_k_is_greater_than_length():
    """
    Test the case when k is greater than the length of the linked list.
    Expected behavior: A ValueError exception should be raised.
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    try:
        ll.kth_from_end(6)
        assert False  # The test should raise an exception, so this line should not be reached
    except ValueError:
        assert True  # The test should raise a ValueError exception


def test_kth_from_end_when_k_and_length_are_same():
    """
    Test the case when k is equal to the length of the linked list.
    Expected behavior: A ValueError exception should be raised.
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    try:
        ll.kth_from_end(5)
        assert False  # The test should raise an exception, so this line should not be reached
    except ValueError:
        assert True  # The test should raise a ValueError exception


def test_kth_from_end_when_k_is_not_positive():
    """
    Test the case when k is not a positive integer.
    Expected behavior: A ValueError exception should be raised.
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    try:
        ll.kth_from_end(-1)
        assert False  # The test should raise an exception, so this line should not be reached
    except ValueError:
        assert True  # The test should raise a ValueError exception


def test_kth_from_end_happy_path():
    """
    Test the "happy path" scenario where k is in the middle of the linked list.
    Expected behavior: The value at the kth position from the end of the list should be returned.
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    assert ll.kth_from_end(2) == 3

# Test empty lists
def test_zip_lists():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll = LinkedList()
    try:
        ll.zip_lists(ll1,ll2)
        assert False  # The test should raise an exception, so this line should not be reached
    except ValueError:
        assert True  # The test should raise a ValueError exception
# Test lists of equal length
def test_zipping_same_length():
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(3)
    ll1.insert(5)

    ll2 = LinkedList()
    ll2.insert(2)
    ll2.insert(4)
    ll2.insert(6)

    expected_result = "{ 5 } -> { 6 } -> { 3 } -> { 4 } -> { 1 } -> { 2 } -> NULL"
    result = LinkedList.zip_lists(ll1, ll2)
    assert str(result) == expected_result

# Test lists of different lengths
def test_zipping_different_length():
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(3)
    ll1.insert(5)
    ll1.insert(70)

    ll2 = LinkedList()
    ll2.insert(2)
    ll2.insert(4)
    ll2.insert(6)

    expected_result = "{ 70 } -> { 6 } -> { 5 } -> { 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL"
    result = LinkedList.zip_lists(ll1, ll2)
    assert str(result) == expected_result

#Test list with list 1 is empty
def test_zipping_ll1_empty():
    ll1 = LinkedList()

    ll2 = LinkedList()
    ll2.insert(2)
    ll2.insert(4)
    ll2.insert(6)

    expected_result = "{ 6 } -> { 4 } -> { 2 } -> NULL"
    result = LinkedList.zip_lists(ll1, ll2)
    assert str(result) == expected_result

# Test list with list 2 is empty
def test_zipping_ll2_empty():
    ll1 = LinkedList()
    ll1.insert(11)
    ll1.insert(12)
    ll1.insert(13)

    ll2 = LinkedList()

    expected_result = "{ 13 } -> { 12 } -> { 11 } -> NULL"
    result = LinkedList.zip_lists(ll1, ll2)
    assert str(result) == expected_result
