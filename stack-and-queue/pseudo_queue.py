from stack import Stack
class PsuedoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            raise Exception("Queue is empty")
        elif self.stack2.is_empty():
            while self.stack1.top:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def __str__(self):
        return str(self.stack1)
    