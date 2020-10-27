try:
    n = int(input())
    for _ in range(n):
        x = int(input())
        c = 0
        t = 5
        while x//t > 0:
            c+=(x//t)
            t*=5
        print(c)
except EOFError:
    pass