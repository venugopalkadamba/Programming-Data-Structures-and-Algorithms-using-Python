# Euclids Algorithm
# Time Complexity: O(log(min(a,b)))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

a, b = map(int, input().split())

print(gcd(max(a,b), min(a,b)))