def reverseInGroups(a,n,k):
    #Your code here
    l = []
    i = 0
    while i<n:
        l = l + a[i:i+k][::-1]
        i+=k
    return l

n, k = map(int, input().strip().split())
l = list(map(int, input().strip().split()))
print(reverseInGroups(l, n, k))