# Question: https://leetcode.com/problems/find-the-duplicate-number

def solve():
    n = int(input())
    l = list(map(int, input().split()))
    arr = [0]*(n+1)
    ans = None
    for number in l:
        arr[number] += 1
        if arr[number] > 1:
            ans = number
    return ans


if __name__ == "__main__":
    solve()
