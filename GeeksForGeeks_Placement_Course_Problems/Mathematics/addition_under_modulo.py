'''
Note:
(a+b)%m = ((a%m)+(b%m))%m
(a-b)%m = ((a%m)-(b%m))%m
(a*b)%m = ((a%m)*(b%m))%m
'''

def sumUnderModulo(a, b, M):
    return ((a%M)+(b%M))%M

a, b = map(int, input().split())
M = (10**9)+7
print(sumUnderModulo(a, b, M))