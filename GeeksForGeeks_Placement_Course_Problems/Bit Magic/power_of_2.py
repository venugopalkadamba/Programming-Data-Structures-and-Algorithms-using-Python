def powerOf2(n):
    temp = n-1
    if n & temp == 0:
        return True
    return False

print(powerOf2(256))