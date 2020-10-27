# Kadenes algorithm

def maxSumSubarray(l):
    max_current = max_global = l[0]
    for i in range(1, len(l)):
        max_current = max(l[i], max_current+l[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

l = list(map(int, input().split()))
print(maxSumSubarray(l))