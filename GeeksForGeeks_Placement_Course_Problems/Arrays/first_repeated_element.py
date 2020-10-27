def firstRepeated(arr, n):
    l = sorted(arr)
    for i in range(n):
        if l.count(arr[i])>1:
            return i+1
    return -1

n = int(input())
l = list(map(int, input().split()))

print(firstRepeated(l, n))