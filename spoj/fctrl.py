powers = [5**i for i in range(1,15)]
n = int(raw_input())
for _ in range(n):
    num = int(raw_input())
    res = 0
    for power in powers:
        res += num/power
    print res
