def solve():
    l = list(map(int, input().split()))
    n = len(l)
    count = [0]*(n+1)
    missing = None
    repeating = None
    s = (n*(n+1)) / 2
    for number in l:
        count[number] += 1
        if count[number] == 1:
            s -= number
        if count[number] > 1:
            repeating = number
    missing = int(s)
    print("Missing", missing)
    print("Repeating", repeating)


solve()
