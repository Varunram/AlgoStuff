def gen_primes(low,upp):
    D = {}
    q = 2
    while q<=upp:
        if q not in D:
            if(q>=low) and (q<=upp):
                print q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

n = input()
i=0
while(i<n):
    low, upp = map(int, raw_input().split())
    gen_primes(low, upp)
    i+=1
