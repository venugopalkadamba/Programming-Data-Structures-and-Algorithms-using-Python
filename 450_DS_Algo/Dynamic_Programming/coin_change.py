def count(S, m, n):
    if n == 0:
        return 1
    if n < 0 or m < 0:
        return 0
    if m > len(S)-1:
        m = m-1
    return count(S, m, n - S[m]) + count(S, m-1, n)

print(count([1,2,3], 3, 4))
print(count([2,3,5,6], 4, 10))