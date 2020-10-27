# Time Complexity: O(n^2)

def selection_sort(arr, length):
    for i in range(length-1):
        min_index = i
        for j in range(i+1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Iteration {i+1}: {arr}")
    return arr

l = list(map(int, input().split()))
print("After Sorting: ",*selection_sort(l,len(l)))