# GAP algorithm

import math

def merge(a,n,b,m):
    total = m + n

    gap = math.ceil(total / 2)

    while gap>0:
        i = 0
        j = i+gap
        while j<(m+n):
            if i<n and j<n:
                if a[j]<a[i]:
                    a[i], a[j] = a[j], a[i]
            elif i>=n and j>=n:
                if b[j-n]<b[i-n]:
                    b[j-n], b[i-n] = b[i-n], b[j-n]
            else:
                if b[j-n]<a[i]:
                    a[i],b[j-n] = b[j-n],a[i]
            i+=1
            j+=1
        if gap == 1:
            break
        gap = math.ceil(gap / 2)

n, m = map(int, input().split())
a = list(map(int ,input().split()))
b = list(map(int, input().split()))

merge(a,n,b,m)

print(a,b)