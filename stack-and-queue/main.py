from queue import Queue

queue1 = Queue()
queue1.enqueue(88)
queue1.enqueue(11)
queue1.enqueue(22)

# queue1.enqueue(1)
print(queue1.dequeue())
print(queue1.peek())
