# Stack and Queue
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Approach & Efficiency
## **Approach**

### **Stack:**

- The stack is implemented using a singly linked list.
- The **`push`** operation adds a new node at the top of the stack by updating the **`next`** pointer of the new node to point to the current top node.
- The **`pop`** operation removes and returns the top node by updating the **`top`** pointer to the next node in the list.
- The **`peek`** operation returns the value of the top node without modifying the stack.
- The **`is_empty`** operation checks if the **`top`** pointer is **`None`** to determine if the stack is empty.

### **Queue:**

- The queue is implemented using a singly linked list with two pointers: **`front`** and **`rear`**.
- The **`enqueue`** operation adds a new node at the rear of the queue by updating the **`next`** pointer of the previous rear node to point to the new node and updating the **`rear`** pointer to the new node if the queue was previously empty.
- The **`dequeue`** operation removes and returns the front node by updating the **`front`** pointer to the next node in the list. If the front and rear pointers become equal, it means the queue becomes empty, so the **`rear`** pointer is also set to **`None`**.
- The **`peek`** operation returns the value of the front node without modifying the queue.
- The **`is_empty`** operation checks if the **`front`** pointer is **`None`** to determine if the queue is empty.

## **Efficiency**

### **Stack:**

- Time Complexity: The **`push`**, **`pop`**, **`peek`**, and **`is_empty`** operations for the stack all have a time complexity of O(1). They directly access or modify the **`top`** pointer without iterating over the entire stack.
- Space Complexity: The space complexity of the stack is O(n), where n is the number of elements in the stack. It requires memory to store the nodes.

### **Queue:**

- Time Complexity: The **`enqueue`**, **`dequeue`**, **`peek`**, and **`is_empty`** operations for the queue all have a time complexity of O(1). They directly access or modify the **`front`** and **`rear`** pointers without iterating over the entire queue.
- Space Complexity: The space complexity of the queue is O(n), where n is the number of elements in the queue. It requires memory to store the nodes.
## Solution
<!-- Show how to run your code, and examples of it in action -->
# stack-queue-animal-shelter
<!-- Description of the challenge -->
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue
Arguments: animal
animal can be either a dog or a cat object.
It must have a species property that is either "cat" or "dog"
It must have a name property that is a string.
dequeue
Arguments: pref
pref can be either "dog" or "cat"
Return: either a dog or a cat, based on preference.
If pref is not "dog" or "cat" then return null.
## Whiteboard Process
<!-- Embedded whiteboard image -->
![whiteboard](./whiteboard.jpg)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
### Big O:
Time :
- enqueue: O(1)
- dequeue: O(1)

Space:
- enqueue: O(n)
- dequeue: O(1)
### Algorithm: 
- define a class Animal Shelter initialize constructor 
- assign Queue to dog and cat create enqueue method
- checks kind of animal and adds It the queue create dequeue method 
- checks kind of animal and removes It from queue 
- returns None if its not dog or cat 
- define Dog class property kind for dog 
- define Cat class property kind for cat 


## Solution
<!-- Show how to run your code, and examples of it in action -->
### Stack
```python
from node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if not self.top:
            raise ValueError("Empty Stack")
        else:
            temp = self.top
            self.size -= 1
            self.top = self.top.next
            return temp.value

    def peek(self):
        if not self.top:
            raise ValueError("Empty Stack")
        else:
            return self.top.value

    def is_empty(self):
        if not self.top:
            return True
        else:
            return False
```
### Queue
``` python
from node import Node
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node


    def dequeue(self):
        if not self.front:
            raise ValueError("Empty Stack")
        if self.front == self.rear:
            self.rear = None

        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value
        

    def peek(self):
        if self.front is None:
            raise ValueError("Empty Stack")
        else:
            return self.front.value
    
    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
```
``` python
class AnimalShelter:
    def __init__(self):
        self.dog = Queue()
        self.cat = Queue()

    def enqueue(self, animal):
        if animal.kind == 'dog':
            self.dog.enqueue(animal)
        elif animal.kind == 'cat':
            self.cat.enqueue(animal)
        else:
            return None

    def dequeue(self, pref):
        if pref == 'dog':
            return self.dog.dequeue()
        elif pref == 'cat':
            return self.cat.dequeue()
        else:
            return None


class Dog:
    def __init__(self):
        self.kind = 'dog'


class Cat:
    def __init__(self):
        self.kind = 'cat'

```

