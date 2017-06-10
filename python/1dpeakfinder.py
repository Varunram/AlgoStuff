def peakfinder(arr):
    mid = len(arr)/2
    if mid ==0:
        return 0
    if arr[mid-1]<=arr[mid]>=arr[mid+1]:
        print arr[mid]
        return mid
    elif arr[mid-1] > arr[mid]:
        return peakfinder(arr[:mid]) + peakfinder(arr[mid:])
    else:
        return peakfinder(arr[mid:]) + peakfinder(arr[:mid])

arr = [3,2,1,-1,-5,5,4]
peakfinder(arr)
