from hashtable import HashTable 
import re
s1 = 'o this is loop, this is loop'
s2 = 'my name is mohamad shareef naser naser'
def repeated_word(sentence: str):
    """Find the first repeated word in a sentence using a HashTable."""
    ht = HashTable()
    words = sentence.split(' ')
    for word in words:
        if ht.has(word):
            return word
        ht.set(word, None)
    return None
print(repeated_word(s2))
