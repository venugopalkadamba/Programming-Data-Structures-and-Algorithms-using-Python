'''
Given an array of integers of size 'n'.
Our aim is to calculate the maximum sum of 'k' 
consecutive elements in the array.
'''
def maxSumConsecutiveSubarray(l, k):
    n = len(l)
    max_sum = -10**5
    for i in range(n-k+1):
        if sum(l[i:i+k])>max_sum:
            max_sum = sum(l[i:i+k])
    return max_sum

l = list(map(int, input().split()))
k = int(input())
print(maxSumConsecutiveSubarray(l, k))