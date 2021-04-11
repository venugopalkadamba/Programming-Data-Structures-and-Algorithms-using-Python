def sort012(arr,n):
    s = [0,0,0]
    for i in arr:
        s[i]+=1
    t = 0
    index = 0
    try:
        while s[t]!=0:
            arr[index] = t
            index += 1
            s[t]-=1
            if s[t] == 0:
                t+=1
    except:
        pass