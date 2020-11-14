def areIsomorphic(s,p):
    m, n = len(s), len(p)

    MAX_CHARS = 256
    if m!=n:
        return False
    marked = [False] * MAX_CHARS
    mapping = [-1] * MAX_CHARS

    for i in range(n):
        if mapping[ord(s[i])] == -1:
            if marked[ord(p[i])] == True:
                return False
            marked[ord(p[i])] = True
            mapping[ord(s[i])] = p[i]
        elif mapping[ord(s[i])] != p[i]:
            return False
    
    return True



s1 = "aab"
s2 = "xyz"
print(areIsomorphic(s1,s2))