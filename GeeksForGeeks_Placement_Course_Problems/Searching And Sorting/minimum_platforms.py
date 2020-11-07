def minimumPlatform(n,arr,dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
    arr = [int(i) for i in arr]
    dep = [int(i) for i in dep]
    arr.sort()
    dep.sort()
    ans, plat = 1, 1
    i, j = 0, 0
    while i<n and j<n:
        if arr[i]<=dep[j]:
            plat+=1
            i+=1
        elif arr[i]>dep[j]:
            plat-=1
            j+=1
        if plat>ans:
            ans = plat
    return ans-1

n = 6
arr = ['0900','0940','0950' ,'1100','1500','1800']
dep = ['0910','1200','1120','1130','1900','2000']
print(minimumPlatform(n,arr,dep))