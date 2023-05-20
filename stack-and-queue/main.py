from queue import Queue

def DuckDuckGoose(k, arr):
    queue1 = Queue()
    for i in arr:
        queue1.enqueue(i)
    while queue1.front.next:
        for i in range(k):
            queue1.enqueue(queue1.dequeue())
        queue1.dequeue()
    return queue1.front.value


print (DuckDuckGoose(3, ['A', 'B', 'C', 'D', 'E']))



