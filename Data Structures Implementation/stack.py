# IMPLEMENTATION OF STACKS

# In python lists can be used as stacks, but it is not recommended, because the lists in pythons are dynamic arrays.
# To overcome this problem collections.dequeue is used ehich are implemented using Doubly Linked Lists

from collections import deque

# We can directly use the deque class but to show the proper representation lets create a Stack classs

class Stack:
    def __init__(self):
        self.stk = deque()
    
    def push(self, val):
        self.stk.append(val)
    
    def pop(self):
        return self.stk.pop()
    
    def is_empty(self):
        return len(self.stk) == 0
    
    def size(self):
        return len(self.stk)

s = Stack()

s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.is_empty())
print(s.size())