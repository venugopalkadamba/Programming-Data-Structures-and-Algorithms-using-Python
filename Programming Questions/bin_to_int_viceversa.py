# Given an integer n, convert it into binary 
# Given a binary representation, convert it into integer

# Integer to Binary
def intToBin(n):
    return str(bin(n))[2:]

# Binary to Integer
def binToInt(n):
    return int(n, 2)

# kth bit set from right
def kthBit(n, k):
    if n & (1 << (k-1)):
        print("SET")
    else:
        print("NOT SET")

m = int(input("Enter the int to bin number: "))
n = input("Enter the bin to int number: ")

print(f"Binary: {intToBin(m)}, Number: {binToInt(n)}")