# Sieve of Eratosthenes

# Time Complexity: O(n*log(log(n)))

from math import *

def generate_primes(n):
    primes = [True]*(n+1)
    primes[0], primes[1] = False, False

    for prime in range(2, int(sqrt(n))+1):
        if primes[prime]:
            for i in range(prime**2, n+1, prime):
                primes[i] = False
    
    for i in range(len(primes)):
        if primes[i]:
            print(i, end = " ")


n = int(input())

generate_primes(n)