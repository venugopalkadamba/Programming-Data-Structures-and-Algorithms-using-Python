def isAnagram(a, b):
    s1, s2 = {}, {}
    
    if len(a) != len(b):
        return False
    
    for i,j in zip(a,b):
        if i not in s1:
            s1[i] = 1
        if j not in s2:
            s2[j] = 1
        if i in s1:
            s1[i] += 1
        if j in s2:
            s2[j] += 1
    
    for i in s1:
        try:
            if s1[i]!=s2[i]:
                return False
        except:
            return False
    return True

a = "allergy"
b = "allergic"
print(isAnagram(a,b))