n, w = map(int, input().split())
a = list(map(int, input().split()))
arr = []
ans = [0 for _ in range(n)]

for i in range(n):
    ans[i] += (a[i] + 1) // 2
    w -= (a[i] + 1) // 2
    arr.append((a[i], i))

if w < 0:
    print(-1)
else:
    arr = list(reversed(sorted(arr)))
    for a, i in arr:
        d = min(w, a - ans[i])
        ans[i] += d
        w -= d
    print(' '.join(map(str, ans)))
