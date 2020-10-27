import math

def quadraticRoots(a, b, c):
    x = (b**2)-(4*a*c)
    if x < 0:
        return [-1]
    root1 = math.floor(((-1*b) + math.sqrt(x))/(2*a))
    root2 = math.floor(((-1*b) - math.sqrt(x))/(2*a))
    return [max(root1, root2), min(root1, root2)]

a, b, c = map(int, input().split())

print(quadraticRoots(a, b, c))