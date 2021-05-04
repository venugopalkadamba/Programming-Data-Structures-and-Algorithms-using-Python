def bestSum(number, array):
    dp = [None] * (number+1)
    dp[0] = []

    for i in range(number+1):
        if dp[i] != None:
            for j in array:
                temp = dp[i].copy()
                temp.append(j)
                if i+j < number+1:
                    if dp[i + j] == None or len(temp) <= len(dp[i + j]):
                        dp[i + j] = temp

    return dp[number]

print(bestSum(7, [5,3,4,7]))
print(bestSum(8, [2,3,5]))
print(bestSum(300, [14,7]))