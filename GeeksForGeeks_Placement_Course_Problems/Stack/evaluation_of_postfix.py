from my_stack import Stack

postfix_expression = "100 200 + 2 / 5 * 7 +".split(" ")

precendence = {
    "+":1,
    "-":1,
    "*":2,
    "/":2,
    "^":3
}

stack = Stack()

for i in postfix_expression:
    print(stack)
    if i not in precendence:
        stack.push(int(i))
    else:
        n1 = stack.topElement()
        stack.pop()
        n2 = stack.topElement()
        stack.pop()
        if i == "+":
            stack.push(n1+n2)
        elif i == "-":
            stack.push(n2-n1)
        elif i == "*":
            stack.push(n2*n1)
        elif i == "/":
            stack.push(n2/n1)
        elif i == "^":
            stack.push(n2**n1)
        
print(stack)