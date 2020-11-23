def XOR_to_n(n):
    rem = n % 4

    if rem == 0:
        return n
    if rem == 1:
        return 1
    if rem == 2:
        return n+1
    if rem == 3:
        return 0

n = 6
print(XOR_to_n(n))