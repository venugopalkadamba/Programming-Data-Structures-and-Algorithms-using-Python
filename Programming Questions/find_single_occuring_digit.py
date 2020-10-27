# Given an array, find the number which occurs once in the array
# Note: n BITWISE_XOR(^) n = 0, n BITWISE_XOR(^) 0 = n

# Time Complexity: O(len(l))
def findSingleOccur(l):
    res = l[0]
    for i in range(1, len(l)):
        res = res ^ l[i]
    return res

l = list(map(int, input().split()))

print(findSingleOccur(l))