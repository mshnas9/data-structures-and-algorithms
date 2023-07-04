from linkedlist import LinkedList


class HashTable:
    def __init__(self, size=10):
        """Initialize a HashTable with a given size."""
        self.size = size
        self.map = [None] * size

    def set(self, key, value):
        """Set a key-value pair in the HashTable."""
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = [key, value]
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key, value])
            else:
                chain = LinkedList()
                existing_pair = self.map[hashed_key]
                new_pair = [key, value]
                self.map[hashed_key] = chain
                chain.add(existing_pair)
                chain.add(new_pair)


    def get(self, key):
        """Get the value associated with a given key in the HashTable."""
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
        """Check if a given key exists in the HashTable."""
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            return False
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                current = self.map[hashed_key].head
                while current:
                    if current.value[0] == key:
                        return True
                    current = current.next  
                return False
            else:
                if self.map[hashed_key][0] == key:
                    return True
        return False

    def keys(self):
        """Get a list of all keys in the HashTable."""
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
        """Return the index of the key based on the hash function."""
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch)
            sum_of_ascii += ch_ascii
        temp = sum_of_ascii * 599
        idx = temp % self.size
        return idx
    
