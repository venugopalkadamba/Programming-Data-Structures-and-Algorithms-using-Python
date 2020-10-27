from heapq import *


def heapsort(l):
    heapify(l)
    return [heappop(l) for i in range(len(l))]

l = list(map(int, input().split()))

heapify(l)

print(l)

heappush(l, 2.5)

x = heappushpop(l, 1.5)

print(x)

print(l)

print("Performing Heapsort:",heapsort(l))