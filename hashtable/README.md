## Summary

This code defines a `HashTable` class that implements a basic hash table data structure. The hash table uses an array to store key-value pairs, and collisions are handled using separate chaining with linked lists.

## Description

The `HashTable` class has the following attributes and methods:

### Class: HashTable

- `__init__(self, size=10)`: Initializes a new instance of the `HashTable` class with the specified size. If no size is provided, the default size is set to 10.
- `set(self, key, value)`: Sets the value associated with the given `key` in the hash table.
- `get(self, key)`: Retrieves the value associated with the given `key` from the hash table.
- `has(self, key)`: Checks if the given `key` exists in the hash table.
- `keys(self)`: Returns a list of all keys stored in the hash table.
- `hash(self, key)`: Computes the hash value for the given `key`.
### Solution
```python
from linkedlist import LinkedList


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.map = [None]*size

    def hash(self, key):
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch)
            sum_of_ascii += ch_ascii
        temp = sum_of_ascii*599
        idx = temp % self.size
        return idx

    def set(self, key, value):
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = [key, value]
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key, value])
            else:
                chain = LinkedList()
                exsiting_pair = self.map[hashed_key]
                new_pair = [key, value]
                self.map[hashed_key] = chain
                chain.add(exsiting_pair)
                chain.add(new_pair)

    def get(self, key):
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            raise KeyError('Key does not exist')
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                current = self.map[hashed_key].head
                while current:
                    if current.value[0] == key:
                        return current.value[1]
                    current = current.next
            else:
                return self.map[hashed_key][1]

    def has(self, key):
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            return False
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                current = self.map[hashed_key].head
                while current:
                    if current.value[0] == key:
                        return True
                return False
            else:
                if self.map[hashed_key][0] == key:
                    return True
        return False

    def keys(self):
        keys_collection = []
        for bucket in self.map:
            if bucket is None:
                pass
            else:
                if isinstance(bucket, LinkedList):
                    current = bucket.head
                    while current:
                        keys_collection.append(current.value[0])
                        current = current.next
                else:
                    keys_collection.append(bucket[0])
        return keys_collection

    def hash(self, key):
        """return the index of the key"""
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch)
            sum_of_ascii += ch_ascii
        temp = sum_of_ascii*599
        idx = temp % self.size
        return idx
```
### Approach & Efficiency

The `HashTable` class uses a hash function that calculates the sum of ASCII values of the characters in a key to determine the index for storing the key-value pairs. Collisions are handled using separate chaining with linked lists.

The time and space complexity of each method are as follows:

| Method                                 | Time Complexity                  | Space Complexity         |
|----------------------------------------|----------------------------------|--------------------------|
| `__init__(self, size=10)`               | O(1)                             | O(1)                     |
| `set(self, key, value)`                 | Average: O(1)<br>Worst: O(n)     | O(1)                     |
| `get(self, key)`                        | Average: O(1)<br>Worst: O(n)     | O(1)                     |
| `has(self, key)`                        | Average: O(1)<br>Worst: O(n)     | O(1)                     |
| `keys(self)`                            | O(n)                             | O(n)                     |
| `hash(self, key)`                       | O(k), where k is the key length  | O(1)                     |

In this implementation, the keys are hashed using the sum of their ASCII values. The hash function provides a constant-time operation. Collisions are resolved by storing key-value pairs in separate linked lists, ensuring efficient retrieval and insertion.

The `set`, `get`, and `has` methods have an average time complexity of O(1) when the hash function distributes the keys evenly across the hash table. However, in the worst case, when all keys hash to the same index, the time complexity can degrade to O(n), where n is the number of elements stored in the hash table.

The `keys` method iterates over each bucket, resulting in a time complexity of O(n) in the average case. The space complexity of the `HashTable` class is O(n), where n is the number of key-value pairs stored in the hash table.

