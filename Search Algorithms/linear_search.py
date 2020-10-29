# Time Complexity: O(n)

def linearSearch(l,n,x):
    for i in range(n):
        if l[i] == x:
            return i
    return -1

n, x = map(int, input().split())
l = list(map(int ,input().split()))
print(linearSearch(l, n, x))