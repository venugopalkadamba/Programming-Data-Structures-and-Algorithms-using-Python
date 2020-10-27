'''
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array and return it. In other words, arrange the elements 
into a sequence such that a1 >= a2 <= a3 >= a4 <= a5..... (considering the increasing lexicographical order).
'''

def convertToWave(A,N):
    for i in range(1, N, 2):
        A[i], A[i-1] = A[i-1], A[i]

N = int(input())
A = list(map(int, input().split()))

convertToWave(A, N)

print(A)