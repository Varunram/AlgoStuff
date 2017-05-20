def cmp(x, j):
    for i in range(0, len(x), 1):
        if x[j][1] < x[i][1]:
            x[j], x[i] = x[i], x[j]
            continue
        if(x[j][1] == x[i][1]):
            if (x[j][0] < x[i][0]):
                x[j], x[i] = x[i], x[j]
            continue
    return x

x=[]
n = int(raw_input())
for rand in range(n):
    n1 = int(raw_input())

    for i in range(n1):
        x.append(map(int, raw_input().split()))
        x = cmp(x, i)
        print x

print x
