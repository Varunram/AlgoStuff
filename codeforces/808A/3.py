n, w =map(int, raw_input().split())
A = map(int, raw_input().split())
B = [0]*len(A)
C = sorted(A, key=int, reverse = True)
for i in range(len(A)):
    if(A[i] %2 ==0):
        B[i] =  A[i]/2
    else:
        B[i] = A[i]/2 + 1

sumb = sum(B)
j =0
res = w-sumb
if sumb >w:
    print -1
else:
    for i in range(len(B)):
        x =  A[A.index(C[i])]
        orig = x
        if x%2 != 0:
            x  = x/2+1
        else:
            x = x/2
        x1 = orig - B[B.index(x)]
        print x1
        if B[B.index(x)] + x1 > orig:
            x1-=1
        if x1 < res:
            B[B.index(x)] += x1
            res -= x1
        else:
            B[B.index(x)] += res
            res = 0
            break;

    if (res>0):
        print -1
    else:
        print ' '.join(map(str, B))
