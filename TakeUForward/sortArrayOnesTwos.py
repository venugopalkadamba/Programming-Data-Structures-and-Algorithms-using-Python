# Question: https://leetcode.com/problems/sort-colors/

# Dutch National Flag Approach
# Three pointer approach
def solve():
    l = list(map(int, input().split()))
    low = 0
    mid = 0
    high = len(l)-1

    while mid <= high:
        temp = l[mid]
        if temp == 0:
            l[low], l[mid] = l[mid], l[low]
            low += 1
            mid += 1
        if temp == 1:
            mid += 1
        if temp == 2:
            l[high], l[mid] = l[mid], l[high]
            high -= 1
            mid += 1

    print(l)


if __name__ == "__main__":
    solve()
