def isPrime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    x = 5
    while x*x <= n:
        if n%x==0 or n%(x+2)==0:
            return False
        x+=6
    return True

n = int(input())
print(isPrime(n))