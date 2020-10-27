import math

def digitsInFactorial(n):
    val = 0
    for i in range(1, n+1):
        val+=math.log10(i)
    return math.floor(val)+1

n = int(input())
print(digitsInFactorial(n))