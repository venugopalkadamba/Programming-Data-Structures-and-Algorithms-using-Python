def exactly3Divisors(n):
    ans = 0
    if n<4:
        return ans
    i = 2
    while(i*i <= n):
        flag = False
        j = 2
        while(j*j <= i):
            if i%j == 0:
                flag = True
                break
            j+=1
        i+=1
        if not flag:
            ans+=1
    return ans

print(exactly3Divisors(int(input())))