from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, data):
        self.q.appendleft(data)
    
    def dequeue(self):
        if self.is_empty():
            return "Empty"
        return self.q.pop()
    
    def que_front(self):
        if self.is_empty():
            return "Empty"
        else:
            return self.q[-1]
    
    def que_rear(self):
        if self.is_empty():
            return "Empty"
        else:
            return self.q[0]
    
    def is_empty(self):
        return len(self.q) == 0
    
    def size(self):
        return len(self.q)

que = Queue()

que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
print(que.dequeue())
print(que.que_front())
print(que.que_rear())
que.dequeue()
que.dequeue()
print(que.dequeue())
print(que.que_front())