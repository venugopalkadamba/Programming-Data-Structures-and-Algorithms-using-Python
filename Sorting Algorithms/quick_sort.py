# Time Complexity: O(n*log(n))
# Worst Case: O(n^2)

def quick_sort(l):
    length = len(l)
    if length<=1:
        return l
    else:
        pivot = l[length//2] # taking middle element as pivot and removing that element
        del l[length//2]
        # pivot = l.pop() # taking last element as pivot and removing that element from the list

    items_greater = []
    items_lower = []
    
    for i in l:
        if i > pivot:
            items_greater.append(i)
        else:
            items_lower.append(i)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

l = list(map(int, input().split()))
print(*quick_sort(l))