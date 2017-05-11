n = int(input())
a = list(map(int, input()))
ans = a[:]
for i in range(n):
    b = [0] * n
    for j in range(n):
        b[j] = (a[(i + j) % n] - a[i]) % 10
    ans = min(ans, b)
print(''.join(map(str, ans)))
