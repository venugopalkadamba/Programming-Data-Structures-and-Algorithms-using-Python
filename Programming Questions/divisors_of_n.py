# Time Complexity = O(root(n))

from math import *

def divisors(n):
    div = set()
    for i in range(1, int(sqrt(n))+1):
        if n%i == 0:
            div.add(i)
            div.add(n // i)
    return list(div)

n = int(input())

print(*divisors(n))