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

size = int(input())
search_value = int(input())
l = list(map(int, input().split()))

print(binary_search(search_value, l))