from collections import deque

stack = deque()

x = "{([])}"

def ispar(x):
    if len(x)==1:
        return False
    stack = deque()
    opened = ['(','[','{']
    closed = [')',']','}']
    for i in x:
        if i in opened:
            stack.append(i)
        else:
            index = closed.index(i)
            if len(stack) > 0 and index == opened.index(stack[-1]):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(ispar(x))