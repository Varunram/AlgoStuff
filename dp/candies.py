''' my sol
def candies(arr):
    count = [1 for i in range(len(arr))]
    for i in range(0, len(arr)-1, 1):
        if arr[i] < arr[i+1]:
            count[i+1]=count[i]+1

    for i in range(len(arr)-1, 1, -1):
        if (arr[i] < arr[i-1]) and (count[i-1] <=count[i]):
            count[i-1] =count[i]+1

    return sum(count)

n = int(raw_input())
res =[]
for _ in range(n):
    x = int(raw_input())
    res.append(x)

print candies(res)
# Fails some testcases though
'''

def get_minimum_candies(candy, count, k):
    if k == 0:
        return 0

    for i in range(1, k):
        c = candy[i]
        left = count[i - 1]
        mid = count[i]
        right = count[i + 1]

        if left < mid <= right:
            c = candy[i - 1] + 1
        elif left < mid and mid > right:
            c = candy[i - 1] + 1
        elif left > mid:
            j = i
            while i > 0 and count[j - 1] > count[j]:
                candy[j - 1] = max(candy[j - 1], candy[j] + 1)
                j -= 1
        elif left == mid or mid == right:
            c = 1

        candy[i] = c

    return candy

n = int(input())
count = []
candy = [1 for j in range(0, n+1)]

for x in range(0, n):
    rating = int(input())
    count.append(rating)

count.append(0)
print(sum(get_minimum_candies(candy, count, n)) - 1)
