def howSum(number, array):
    dp = [None] * (number+1)
    dp[0] = []

    for i in range(number+1):
        if dp[i] != None:
            for j in array:
                index = i+j
                if index < number+1:
                    dp[index] = dp[i].copy()
                    dp[index].append(j)
    # print(dp)
    return dp[number]

print(howSum(7, [5,3,4,7]))
print(howSum(8, [2,3,5]))
print(howSum(300, [14,7]))