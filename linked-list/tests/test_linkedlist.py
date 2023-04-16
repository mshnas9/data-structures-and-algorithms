from linkedlist import LinkedList
import pytest
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
