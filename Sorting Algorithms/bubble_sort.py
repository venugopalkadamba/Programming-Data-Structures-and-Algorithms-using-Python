# Time Complexity: O(n^2)

def bubble_sort(arr, length):
    for i in range(length):
        for j in range(length-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"Iteration {i+1}: {arr}")
    return arr

l = list(map(int, input().split()))
print(bubble_sort(l ,len(l)))