'''
Given an array A of positive integers. Your task is to find the leaders in the array.

Note: An element of array is leader if it is greater than or equal to all the elements to 
its right side. Also, the rightmost element is always a leader. 
'''
def leaders(a,n):
    leader = a[-1]
    l = [a[-1]]
    for i in range(n-2,-1,-1):
        if a[i] >= leader:
            leader = a[i]
            l.append(leader)
    return l[::-1]

n = int(input())
l = list(map(int, input().split()))
print(leaders(l, n))