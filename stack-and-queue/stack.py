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

