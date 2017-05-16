def lcs(X , Y):
    m = len(X)
    n = len(Y)

    L = [[None]*(n+1) for i in xrange(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    return L[m][n]

n = int(raw_input())
for rand in range(n):
    x = map(int, raw_input().split())
    x1 = "".join(map(str, x))
    max1 = 0
    while(True):
        j = map(int, raw_input().split())
        if (j[0] == 0):
            break;
        j1 = "".join(map(str, j))
        res = int(lcs(j1,x1))
        if max1<res:
            max1 = res
    if max1>1:
        print max1-1
    else:
        print 0
