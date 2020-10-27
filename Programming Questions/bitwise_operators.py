# & - bitwise operator AND
# | - bitwise operator OR
# ~ - bitwise operator NOT
# ^ - bitwise operator XOR
# >> - bitwise operator Right Shift: divide in power of 2
# << - bitwise operator Left Shift: multiply in power of 2

def even_odd(n):
    if n&1:
        return "ODD"
    else:
        return "EVEN"

def multiply_pow_2(m, n):
    return m<<n

def divide_pow_2(m, n):
    return m>>n