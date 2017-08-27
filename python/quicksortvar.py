def quicksort(arr, l, r, pivotchoice):
    if l>=r:
        return 0
    else:
        comparisons = r-l-1
        if pivotchoice == 'FIRST':
            pass
        elif pivotchoice == 'LAST':
            arr[l], arr[r-1] = arr[r-1], arr[l]
        elif pos == 'MEDIAN':
            mid = l+comparisons / 2
            if arr[l]<arr[mid]<arr[r-1] or arr[r-1]<arr[mid]<arr[l]:
                arr[l], arr[mid] = arr[mid], arr[l]
            elif arr[mid]<arr[r-1]<arr[l] or arr[l]<arr[r-1]<arr[mid]:
                arr[l], arr[r-1] = arr[r-1], arr[l]

        pivot = arr[l]
        i = l+1
        for j in range(l+1, r):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[l], arr[i-1] = arr[i-1], arr[l]
        comparisons += quicksort(arr, l, i-1, pivotchoice)
        comparisons += quicksort(arr,i, r, pivotchoice)
        return comparisons


with open('quicksort.txt') as f:
    arr1= map(int, (line for line in f))
    for pos in ('FIRST', 'MEDIAN', 'LAST'):
        arr=  arr1[:]
        print pos, quicksort(arr,0,len(arr), pos)
