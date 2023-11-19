def si(num):
    if num > 0:
        return 1
    return -1


x = int(input())
for i in range(x):
    y = int(input())
    z = [int(i) for i in input().split()]
    temp = z[0]
    # sig = si(temp)
    su = 0
    for j in range(1, y):
        if si(temp) == si(z[j]):
            temp = max(temp, z[j])
        else:
            su += temp
            temp = z[j]
    print(su+temp)
