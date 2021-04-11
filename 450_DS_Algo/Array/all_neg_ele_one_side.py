l = list(map(int, input().split()))

left = 0
right = len(l) - 1

while left <= right:
    if l[left] > 0 and l[right] < 0:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    elif l[right] < 0 and l[left] < 0:
        left += 1
    elif l[right] > 0 and l[left] > 0:
        right += 1
    else:
        right -= 1
        left+=1

print(l)