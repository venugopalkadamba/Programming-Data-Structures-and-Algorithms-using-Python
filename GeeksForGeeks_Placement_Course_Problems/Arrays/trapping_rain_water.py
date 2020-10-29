def trappingWater(arr,n):
    ans = 0

    left = [0]*n
    right = [0]*n
    
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])
    
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])
    
    # print(arr, left, right)
    
    for i in range(n):
        ans += min(left[i], right[i])-arr[i]
    
    return ans

# n = int(input())
# l = list(map(int, input().split()))
l = list(map(int,"8 8 2 4 5 5 1".split()))
print(trappingWater(l, len(l)))