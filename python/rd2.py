def countingSort(arr, radix):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(n):
        digit = (arr[i]/radix)
        count[(digit)%10] += 1
    for i in range(10):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        digit = (arr[i]/radix)
        output[count[digit%10]-1] = arr[i]
        count[(digit)%10] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]
    print arr

def radixSort(arr):
    max1 = max(arr)
    radix = 1
    while max1/radix > 0:
        countingSort(arr,radix)
        radix *= 10
    return arr

print radixSort([565, 54, 32, 21, 2, 24, 56, 678])
