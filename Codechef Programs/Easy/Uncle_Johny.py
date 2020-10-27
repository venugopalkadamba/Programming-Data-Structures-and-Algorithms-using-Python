for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    k = int(input())
    val = l[k-1]
    print(sorted(l).index(val)+1)
