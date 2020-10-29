# This function brings all the negative numbers to left side of the array and the positive numbers to right side of array
def divideArray(l, n):
    j = 0
    for i in range(n):
        if l[i]<0:
            l[i], l[j] = l[j], l[i]
            j+=1
    return l, j

def findSmallestPositiveMissing(l ,index, n):

    # making all the elements at l[index+l[i]-1] as negative if they are accessible and are positive
    for i in range(index, n):
        temp = abs(l[i])
        if (index+temp)<=n and l[index+temp-1]>0:
            l[index+temp-1] = -1*l[index+temp-1]
    
    flag = True
    for i in range(index, n):
        if l[i]>0:
            flag = False
            ans = i-index+1
            break
    
    if flag:
        ans = n+1
    
    return ans

t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l, index = divideArray(l, n) # index variable stores the index from which the positive numbers starts
    print(index, l)
    print(findSmallestPositiveMissing(l, index, n))