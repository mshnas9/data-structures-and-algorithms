from node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)

        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front == None:
            return "This queue is empty"
        if self.front == self.rear:
            self.rear = None
        temp = self.front
        self.front = self.front.next
        temp.next = None

        return temp.value

    def peek(self):
        if self.front == None:
            return "this queue is empty"
        return self.front.value
