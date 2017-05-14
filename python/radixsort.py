def countingSort(x, radix):
    length = len(x)
    output = [0] * (length)
    count = [0] * (10)
    for i in range(length):
        digit = (x[i]/radix)
        count[(digit)%10] += 1
    for i in range(10):
        count[i] += count[i-1]
    for i in range(length-1, -1, -1):
        digit = (x[i]/radix)
        output[count[digit%10]-1] = x[i]
        count[(digit)%10] -= 1
    for i in range(len(x)):
        x[i] = output[i]
    print x

def radixSort(x):
    radix = 1
    while max(x)/radix > 0:
        countingSort(x,radix)
        radix *= 10
    return x

print radixSort([100,1,46,23,23, 676, 878])
