def getEquilibriumIndex(l):
    n = len(l)
    total_sum = sum(l)
    left_sum = 0
    index = -1
    for i in range(n):
        total_sum-=l[i]
        if left_sum == total_sum:
            index = i
            break
        left_sum+=l[i]
    return index

l = list(map(int, input().split()))
print(getEquilibriumIndex(l))