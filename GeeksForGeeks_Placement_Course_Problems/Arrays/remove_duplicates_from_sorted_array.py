def remove_duplicate(n, l):
    a = [l[0]]
    i = 1
    fn = 0
    while i<n:
        if a[fn]!=l[i]:
            a.append(l[i])
            fn+=1
        i += 1
    
    # modifying original array
    for i in range(fn+1):
        l[i] = a[i]
    
    return fn+1

l = list(map(int, input().split()))

n = remove_duplicate(len(l),l)
print([l[i] for i in range(n)])