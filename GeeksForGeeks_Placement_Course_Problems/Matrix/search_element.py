# Search Element in Row-wise and Column-wise Sorted Matrix

def search(a, rows, cols, k):
    i, j = 0, cols-1
    while i<rows and j>=0:
        if a[i][j] == k:
            return (i,j)
            break
        elif k > a[i][j]:
            i+=1
        else:
            j-=1
    return -1

a = [
    [1,2,3,4],
    [5,6,8,9]
]

rows = 2
cols = 4

k = 2

print(search(a, rows, cols, k))