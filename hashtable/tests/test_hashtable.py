import pytest 
from hashtable import HashTable

def test_set():
    """test set method"""
    ht = HashTable()
    ht.set('hello', 'world')
    assert ht.map[8] == ['hello', 'world']

def test_get():
    """test get method"""
    ht = HashTable()
    ht.set('hello', 'world')
    assert ht.get('hello') == 'world'

def test_get_key_error():
    """test get method when the key does not exist"""
    ht = HashTable()
    ht.set('hello', 'world')
    with pytest.raises(KeyError):
        ht.get('code')

def test_has_with_key():
    """test has method if there is key"""
    ht = HashTable()
    ht.set('hello','world')
    assert ht.has('hello') == True    

def test_has_without_key():
    """test has method if there is no key exist"""
    ht = HashTable()
    ht.set('hello','world')
    assert ht.has('code') == False    

def test_keys_empty():
    """test keys method when hashtable is empty"""
    ht = HashTable()
    assert ht.keys()==[]
    
def test_keys_collection():
    """test keys_collection with values"""
    ht = HashTable()
    ht.set('hello','world')
    ht.set('Mohamad','Shareef')
    ht.set('ASAC','LTUC')
    assert ht.keys() == ['ASAC', 'Mohamad', 'hello']
    
def test_keys_with_collision():
    """test keys_collection with collision inside hashmap"""
    ht = HashTable()
    ht.set('pool','water')
    ht.set('loop','fire')
    ht.set('hello','world')
    assert ht.keys() == ['pool', 'loop', 'hello']


def test_hash():
    """"test hash function, it suppposed to return the index of the key"""
    ht = HashTable()
    assert ht.hash('hello') == 8
