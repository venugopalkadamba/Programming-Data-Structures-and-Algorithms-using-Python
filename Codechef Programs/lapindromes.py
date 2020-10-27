try:
    for _ in range(int(input())):
        s = input()
        n = len(s)
        if n&1:
            left = s[:n//2]
            right = s[(n//2)+1:]
        else:
            left = s[:n//2]
            right = s[n//2:]
        if sorted(left) == sorted(right):
            print("YES")
        else:
            print("NO")
except EOFError:
    pass