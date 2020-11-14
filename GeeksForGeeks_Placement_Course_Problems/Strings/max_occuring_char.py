def getMaxOccurringChar(s):
    l = list(s)
    counts = {}
    for i in l:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    max_count = 0
    max_char = "z"
    for i in counts:
        # print(i, max_char, i<=max_char)
        if counts[i] >= max_count and i <= max_char:
            max_count = counts[i]
            max_char = i
    return max_char

s = "testsample"
print(getMaxOccurringChar(s))