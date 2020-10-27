'''
Given a number n the task is to complete the function which returns an integer 
denoting the smallest number evenly divisible by each number from 1 to n.

Approach: gcd(a,b)*lcm(a,b) = a*b
We need to find the lcm for range(1,n+1)
'''

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def getSmallestDivNum(n):
    l = range(1,n+1)
    ans = l[0]
    for i in l:
        ans = (ans*i)/(gcd(max(ans,i),min(ans,i)))
    return int(ans)

n = int(input())
print(getSmallestDivNum(n))