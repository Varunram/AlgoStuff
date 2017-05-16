n = int(input())

for xt in range (n):
	a,b,p,q = map(int, raw_input().split())
	start = 1
	end = 1000000000

	ans = -1
	while (start <= end):
		mid = (start + end) // 2;
		y = q*mid-b;
		x = mid*p-a;
		if (x <= y and x >= 0 and y >= 0):
			ans = y
			end=mid-1
		else:
			start=mid+1

	print(ans)
