'''
Time Complexity: O(n)
'''

def subArraySum(arr, n, su):
    current_sum = arr[0]
    start = 0

    i = 1
    while i <= n:
        while current_sum > su and start < i-1:
            current_sum -= arr[start]
            start += 1
        
        if current_sum == su:
            print(start+1, i)
            return
        
        if i < n:
            current_sum+=arr[i]
        i+=1
    
    print(-1)
    return

n, s = map(int, input().split())
l = list(map(int, input().split()))

subArraySum(l, n, s)