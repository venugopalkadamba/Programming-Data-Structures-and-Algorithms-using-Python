array = list(map(int, input().split()))

# using slicing in python
ans = array[::-1]
print(ans)

# using the logic
n = len(array)

for i in range(n // 2):
    array[i], array[n-i-1] = array[n-i-1], array[i]

print(array)