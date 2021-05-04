def canSum(number, array):
    dp = [False] * (number+1)
    dp[0] = True

    for i in range(number+1):
        if dp[i] == True:
            for j in array:
                index = i+j
                if index < number+1:
                    dp[index] = True
    
    return(dp[number])

print(canSum(7, [5,3,4,7]))
print(canSum(300, [14,7]))