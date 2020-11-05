# Time Complexity: O(log(n))

def peakElementUtil(l, low, high, n):
    mid = low + (high-low)/2
    mid = int(mid)
    if ((mid==0 or l[mid-1]<=l[mid]) and (mid==n-1 or l[mid+1]<=l[mid])):
        return mid
    elif (mid>0 and l[mid-1]>l[mid]):
        return peakElementUtil(l, low, (mid-1),n)
    else:
        return peakElementUtil(l, (mid+1), high, n)

def peakElement(l, n):
    return peakElementUtil(l, 0, n-1, n)

n = int(input())
l = list(map(int, input().split()))
peakElement(l, n)