def binarySearch(l, n, x):
    left = 0
    right = n-1
    ans = 0
    while left <= right:
        mid = (left+(right-1))//2
        if l[mid] == x:
            return mid
        if x >= l[mid]:
            left = mid+1
        elif x < l[mid]:
            right = mid-1
    return ans

n, x = map(int, input().split())
l = list(map(int, input().split()))
firstIndex = binarySearch(l, n, x)
lastIndex = binarySearch(l[::-1], n, x)
ans = (n-lastIndex) - firstIndex + 1
print(ans)