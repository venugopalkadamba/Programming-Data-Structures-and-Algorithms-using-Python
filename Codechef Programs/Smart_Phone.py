try:
    l = []
    n = int(input())
    for _ in range(n):
        l.append(int(input()))
    l = sorted(l)[::-1]
    print(max([l[i]*(i+1) for i in range(n)]))
except EOFError:
    pass