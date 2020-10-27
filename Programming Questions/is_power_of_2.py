# Given an integer n, print whether it is in power of 2

def is_power_2(n):
    # Time Complexity: O(1)
    if n <= 0:
        return False
    a = n
    b = not(n & (n-1))
    return a and b

n = int(input())

print(is_power_2(n))