from hashtable import HashTable 
import re
def repeated_word(sentence: str):
    """Find the first repeated word in a sentence using a HashTable."""
    ht = HashTable()
    words = re.findall(r'\w+', sentence.lower())
    for word in words:
        if ht.has(word):
            return word
        ht.set(word, None)
    return None
