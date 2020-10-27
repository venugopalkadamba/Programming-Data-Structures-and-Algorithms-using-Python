def rotateArr(A,D,N):
    x = A[:D]
    del A[:D]
    A+=x

N, D = map(int, input().split())
A = list(map(int, input().split()))
rotateArr(A, D, N)
print(A)