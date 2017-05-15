def gen_primes(low,upp):
    D = {}
    a=[]
    q = 2
    while q<=upp:
        if q not in D:
            a.append(q)
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1
    return a
n = input()
j=0
x = gen_primes(1,32000)
print x

while(j<n):
    low, upp = map(int, raw_input().split())
    for i in x:
        if (i>=low) and (i<=upp):
            print i
    j+=1
