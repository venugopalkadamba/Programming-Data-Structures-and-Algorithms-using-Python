from collections import deque

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
    
    def top(self):
        return self.stk[-1]

def is_balanced(s):
    brac = {
        ')':'(',
        '}':'{',
        ']':'[',
    }
    
    stk = Stack()

    for i in s:
        if i == '(' or i == '[' or i == '{':
            stk.push(i)
        if i == ')' or i == ']' or i == '}':
            
            if stk.is_empty():
                return False

            if brac[i] == stk.top():
                stk.pop()
    return stk.is_empty()

s = input()

print(is_balanced(s))