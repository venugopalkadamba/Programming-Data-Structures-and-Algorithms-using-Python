# Time Complexity: O(n*log(n))

def merge_sort(l):
    if len(l)>1:
        mid = len(l) // 2
        
        left = l[:mid]
        right = l[mid:]

        merge_sort(left)
        merge_sort(right)
        
        
        # code for merging the lists
        i = j = k = 0
        
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i+=1
                k+=1
            else:
                l[k] = right[j]
                j+=1
                k+=1
        while i < len(left):
            l[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            l[k] = right[j]
            k+=1
            j+=1

l = list(map(int, input().split()))
merge_sort(l)
print(*l)