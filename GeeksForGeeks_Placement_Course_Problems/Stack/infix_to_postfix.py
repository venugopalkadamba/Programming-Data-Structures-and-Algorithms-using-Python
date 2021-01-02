from my_stack import Stack

operators = ("+","-","*","/","^","(",")")
stack = Stack()

expression = "a+b*(c^d-e)^(f+g*h)-i"


precendence = {
    "+":1,
    "-":1,
    "*":2,
    "/":2,
    "^":3
}

postfix = ""

def checkPrecedence(element):
    try:
        return True if precendence[element] <= precendence[stack.topElement()] else False
    except:
        return False

for i in expression:
    if i not in operators:
        postfix += i
    elif i == "(":
        stack.push(i)
    elif i == ")":
        while not stack.isEmpty() and stack.topElement() != "(":
            postfix += stack.topElement()
            stack.pop()
        if not stack.isEmpty() and stack.topElement() == "(":
            stack.pop()
    else:
        while not stack.isEmpty() and checkPrecedence(i) and (stack.topElement() != "(" or stack.topElement() != ")"):
            postfix += stack.topElement()
            stack.pop()
        stack.push(i)

while not stack.isEmpty():
    postfix += stack.topElement()
    stack.pop()

print(f"Infix Expression is {expression}\nPostfix Expression is {postfix}")