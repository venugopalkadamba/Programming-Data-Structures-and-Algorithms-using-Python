def immediateSmaller(arr,n,x):
    min_diff = 10**7
    element = 0
    for i in range(n):
        if (x-arr[i])>0 and (x-arr[i])<min_diff:
            min_diff = x-arr[i]
            element = arr[i]
    if min_diff == 10**7:
        return -1
    else:
        return element

n, x = map(int, input().split())
l = list(map(int, input().split()))
print(immediateSmaller(l, n, x))