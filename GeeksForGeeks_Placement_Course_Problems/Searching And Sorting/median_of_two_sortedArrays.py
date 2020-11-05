import math
def findMedianSortedArrays(arr1, n1, arr2, n2):
    '''
    arr1: shorter array
    n1:   len of arr
    arr2: larger array
    n2:   len of array
    return: median
    '''
    l = []
    i, j = 0,0
    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            l.append(arr1[i])
            i+=1
        else:
            l.append(arr2[j])
            j+=1
    
    while i<n1:
        l.append(arr1[i])
        i+=1
    
    while j<n2:
        l.append(arr2[j])
        j+=1
    
    if (n1+n2)%2==0:
        mid = (n1+n2)//2
        return math.floor((l[mid-1]+l[mid])/2)
    else:
        mid = (n1+n2)//2
        return l[mid]