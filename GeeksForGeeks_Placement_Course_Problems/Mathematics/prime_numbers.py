# Sieve of Eratosthenes
# Time Complexity: O(n*log(log(n)))

def prime_numbers(n):
    prime_list = [True for _ in range(n+1)]
    p = 2
    while p*p <= n:
        if prime_list[p]:
            for i in range(p*2, n+1, p):
                prime_list[i] = False
        p += 1
    prime_list[0], prime_list[1] = False, False

    for i in range(n+1):
        if prime_list[i]:
            print(i, end = " ")

prime_numbers(int(input()))