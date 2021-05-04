def canConstruct(string, wordBank, memo = {}):
    if string in memo:
        return memo[string]
    if string == "":
        return True
    for s in wordBank:
        if string.startswith(s):
            new_string = string.replace(s, "")
            if canConstruct(new_string, wordBank, memo):
                memo[string] = True
                return True
    memo[string] = False
    return False

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))