from node import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,value):

        node = Node(value)
        
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
                current.next = node
        
    def includes(self,value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def __str__(self):
        current = self.head
        string = ''
        while current is not None:
            string += f'{{ {current.value} }} -> '
            current = current.next
        string += 'NULL'
        return string