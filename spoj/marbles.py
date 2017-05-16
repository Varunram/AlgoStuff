def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok / ktok
    else:
        return 0

n = int(raw_input())
for rand in range(n):
    n1, n2 = map(int, raw_input().split())
    print choose(n1-1, n2-1)
