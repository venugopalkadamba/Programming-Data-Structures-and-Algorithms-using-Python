from collections import deque

l = list(input().split(" "))

stack = deque()

for i in l:
    stack.append(i)

for i in range(len(l)):
    print(stack.pop())