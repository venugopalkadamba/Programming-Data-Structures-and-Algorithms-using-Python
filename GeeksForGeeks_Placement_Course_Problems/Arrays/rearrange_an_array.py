def arrange(arr, n): 
    l = []
    for i in range(n):
        l.append(arr[i] + (arr[arr[i]]*n))
    
    for i in range(n):
        arr[i] = l[i]//n
    del l
    
n = int(input())
l = list(map(int, input().split()))
arrange(l,n)