# Given an integer n, find the number of 1's in its binary form

# Time Complexity: O(n)
def bruteforce_approach(n):
    return bin(n)[2:].count('1')

# Time Complexity: O(log(n))
def count_1s(n):
    c = 0
    while(n):
        c+=1
        n = n & (n-1)
    return c

n = int(input())
print(count_1s(n))