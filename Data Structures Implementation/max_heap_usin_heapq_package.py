from heapq import *

# By default heapq implements min heap, inorder to create max heap using heapq, multiply all the elements with -1

def max_heap(l):
    h = []
    for i in l:
        heappush(h, -1*i)
    return h

l = list(map(int, input().split()))

h = max_heap(l)

max_h = [-1*i for i in h]

print(max_h)