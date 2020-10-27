def modInverse(a,m):
    for i in range(1, m):
        if ((a*i)%m) == 1:
            return i
    return -1

a, m = map(int, input().split())
print(modInverse(a, m))