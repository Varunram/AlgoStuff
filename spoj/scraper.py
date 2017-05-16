def find(i):
    if parent[i]!=i:
        parent[i] = find(parent[i])
    return parent[i]

def union(i,j):
    while(parent[i]!=i):
        i = parent[i]
    while(parent[j]!=j):
        j = parent[j]
    if(rank[i]<rank[j]):
        parent[i] = j
    else:
        parent[j] = i
        if rank[i] == rank[j]:
            rank[i]+=1

num = int(raw_input())
for rand in xrange(num):
    F,E,A,B = map(int, raw_input().split())
    rank = [0]*F
    parent = list(xrange(F))
    for i in xrange(E):
        X,Y = map(int, raw_input().split())
        for j in xrange(Y,F,X):
            union(Y,j)
    if find(A) == find(B):
        print 'It is possible to move the furniture'
    else:
        print 'The furniture cannot be moved'
