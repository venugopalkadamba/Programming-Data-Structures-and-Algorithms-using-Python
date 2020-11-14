def reverseWords(s):
    return '.'.join(s.split(".")[::-1])

S = "i.like.this.program.very.much"
print(reverseWords(S))