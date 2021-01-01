from collections import deque

class Stack:
    def __init__(self, elements=[]):
        self.array = deque(elements)
    
    def isEmpty(self):
        return True if len(self.array) == 0 else False

    def topElement(self):
        return self.array[-1] if not self.isEmpty() else None
    
    def push(self, element):
        self.array.append(element)
    
    def pop(self):
        if not self.isEmpty():
            return self.array.pop()

    def __str__(self):
        return " ".join([str(i) for i in self.array])

# stack = Stack(["a","b","c"])
# print(stack, "\ntop ==>", stack.topElement())
# stack.push("d")
# stack.push("e")
# stack.push("f")
# print(stack, "\ntop ==>", stack.topElement())
# stack.pop()
# print(stack, "\ntop ==>", stack.topElement())
# stack.pop()
# print(stack, "\ntop ==>", stack.topElement())