from collections import deque

stack = deque()

stack.append("venu")
stack.append("gopal")
stack.append("lava")

print("Tnitial Stack:", stack)

print("pop() function to pop")
print(stack.pop())
print(stack.pop())

print("After all the elements are popped", stack)