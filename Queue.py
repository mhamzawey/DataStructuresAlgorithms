class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.append(val)
        return val

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]



queue = Queue()

print(queue.enqueue(5))
print(queue.enqueue(7))
print(queue.enqueue(8))
print(queue.enqueue(9))

print("peek" + str(queue.peek()))

print (queue.dequeue())
print (queue.dequeue())
print (queue.dequeue())
print (queue.dequeue())