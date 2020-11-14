def areRotations(s1,s2):
    n = len(s1)

    if s1 == s2:
        return True
    for i in range(len(s1)-1):
        s1 = s1[-1] + s1[:n-1]
        if s1 == s2:
            break
    else:
        return False
    return True

s1 = "geeksforgeeks"
s2 = "forgeeksgeeks"
print(areRotations(s1,s2))