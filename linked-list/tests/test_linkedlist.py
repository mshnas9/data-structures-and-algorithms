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
 

def test_kof2():
    excepted = 3
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(7)
    ll.append(9)
    actual = ll.kth_from_end(1)
    assert excepted == actual
