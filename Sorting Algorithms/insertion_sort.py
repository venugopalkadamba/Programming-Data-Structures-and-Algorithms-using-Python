# Time Comlexity: O(n^2)

def insertion_sort(arr, length):
    for i in range(1, length):
        key_element = arr[i]
        j = i-1
        while j >= 0 and key_element < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j+1] = key_element
        print(f"Iteration {i+1}: {arr}")
    return arr

l = list(map(int, input().split()))
print(insertion_sort(l, len(l)))