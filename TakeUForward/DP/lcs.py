'''
Longest Common Subsequence Problem
'''

# Basic recusrsive approach
def lcs(i, j, string1, string2):
    if i>=len(string1) or j>=len(string2):
        return 0
    if string1[i] == string2[j]:
        return 1+lcs(i+1, j+1, string1, string2)
    else:
        left = lcs(i+1, j ,string1, string2)
        right = lcs(i, j+1, string1, string2)
        return max(left, right)

# DP Approach
# Here dp is a 2-dimensional matrix (m,n) with all values initially as -1
# m -> size of string1 and n -> size of string2
def dplcs(i, j, string1, string2, dp):
    if i>=len(string1) or j>=len(string2):
        return 0
    
    if dp[i][j]!=-1:
        return dp[i][j]

    if string1[i] == string2[j]:
        return 1+dplcs(i+1, j+1, string1, string2)
    
    else:
        left = dplcs(i+1, j ,string1, string2)
        right = dplcs(i, j+1, string1, string2)
        dp[i][j] =  max(left, right)
        return dp[i][j]

s1 = "Venu"
s2 = "sVnu"
print(lcs(0,0,s1,s2))