def transpose(a, rows, columns):
    temp = []
    for i in range(columns):
        temp.append([])
        for j in range(rows):
            temp[i].append(a[j][i])
        print(temp[i])


rows = 4
columns = 4
a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

transpose(a, rows, columns)