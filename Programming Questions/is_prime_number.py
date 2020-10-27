# Time Complexity: max is O(root(n))

def is_prime_number(n):

    # Handling Base Cases
    if n == 0 or n == 1: # O(1)
        return False
    
    if n == 2 or n == 3: # O(1)
        return True
    
    if n%2 == 0 or n%3 == 0: # O(1)
        return False
    
    for i in range(5, int(n**0.5)+1):
        if n%i == 0 or n%(i+2) == 0:
            break
    else:
        return True
    
    return False

n  = int(input())

print(is_prime_number(n))