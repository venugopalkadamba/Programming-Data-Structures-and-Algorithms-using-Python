def logBase2(n):
    ans = 0
    while n>>1:
        ans+=1
        n = n>>1
    return ans

n = 18
print(2**(logBase2(n)))