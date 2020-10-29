# Time Complexity: O(log(n) to base 3)

def ternarySearch(l, r, x, arr):
    while r>=l:
        mid1 = l + (r-1) // 3
        mid2 = r - (r-1) // 3

        if arr[mid1] == x:
            return mid1
        
        if arr[mid2] == x:
            return mid2
        
        if x < arr[mid1]:
            r = mid1 - 1
        elif x > arr[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
    
    return -1

n, x = map(int, input().split())
l = list(map(int ,input().split()))
print(ternarySearch(0, n-1, x, l))