try:
    for _ in range(int(input())):
        n = int(input())
        l = list(map(int, input().split()))
        c = 1 # first car is always free to go
        for i in range(1,n):
            if l[i]>l[i-1]:
                # if the current car is faster than previous, it has to slow down
                l[i] = l[i-1]
            else:
                # else free to go
                c+=1
        print(c)
except EOFError:
    pass