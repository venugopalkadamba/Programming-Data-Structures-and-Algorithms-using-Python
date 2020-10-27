def prefixSumArray(l):
    psa = []
    psa.append(l[0])
    for i in range(1, len(l)):
        psa.append(psa[i-1]+l[i])
    return psa

l = list(map(int, input().split()))

print(prefixSumArray(l))