def missingAndRepeating(l, n):
    repeating_num, missing_num = 0, 0
    for i in range(n):
        temp = l[abs(l[i])-1]
        if temp < 0:
            repeating_num = abs(l[i])
        else:
            l[abs(l[i])-1] = -1*l[abs(l[i])-1]
    
    for i in range(n):
        if l[i]>0:
            missing_num = i+1
    print(repeating_num, missing_num)

# l = [2,3,2,1,5]
l = list(map(int, input().split()))
missingAndRepeating(l, len(l))