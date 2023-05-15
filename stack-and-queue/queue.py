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