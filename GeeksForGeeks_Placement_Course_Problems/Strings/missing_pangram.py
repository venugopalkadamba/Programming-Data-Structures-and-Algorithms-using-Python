def missingPanagram(s):
    alphas =  "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    s = s.lower()
    for i in alphas:
        if i not in s:
            ans+=i
    return ans

s = input()
print(missingPanagram(s))