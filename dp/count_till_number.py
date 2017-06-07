def counter(arr, n):
    count = [0 for i in range(n+1)]
    count[0] = 1
    for i in range(1,n+1,1):
        for j in arr:
            if i>=j:
                count[i] += count[i-j]
        print count
    print count[n]


arr = [1,5,6]
n = 7
counter(arr,n)
