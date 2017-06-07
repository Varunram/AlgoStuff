# Kadane's algorithm
def contig(arr):
    maxendinghere = 0
    maxsofar = float('-inf')

    for i in arr:
        maxendinghere += i
        if maxendinghere > maxsofar:
            maxsofar = maxendinghere
        if maxendinghere<0:
            maxendinghere = 0
    return maxsofar


def noncontig(arr):
    for j in range(len(arr)):
        if arr[j]>0:
            break
    incl = old_incl = arr[j]
    for i in range(j+1, len(arr)):
        incl += arr[i]
        if incl > old_incl:
            old_incl = incl
        else:
            incl -=arr[i]

    if (old_incl >=0):
        return old_incl
    else:
        return max(arr)

t = int(raw_input())

for rand in range(t):
    n = int(raw_input())
    arr = map(int, raw_input().split())
    print contig(arr), noncontig(arr)
