# Time Complexity: O(log(n))

def binary_search(n, l):
    
    left = 0
    right = len(l) - 1

    while left <= right:
        
        mid = left + (right-1) // 2

        if l[mid] == n:
            return mid
        elif n < l[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# Using Recursion
def bin_search(A, left, right, k):
    if right >= left:
        mid = (left + right)//2
        if A[mid] == k:
            return mid
        elif k >= A[mid]:
            left = mid+1
            return bin_search(A, left, right, k)
        elif k < A[mid]:
            right = mid-1
            return bin_search(A, left, right, k)
    return -1

size = int(input())
search_value = int(input())
l = list(map(int, input().split()))

print(binary_search(search_value, l))