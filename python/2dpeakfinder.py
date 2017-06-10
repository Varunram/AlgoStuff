# BUG: arr1 view top to bottom. tilt head to udnerstand
def find_max(arr1):
    max1 = max(arr1)
    return max1, arr1.index(max1)


def peakfinder(arr, start, end):
    print arr
    if end - start <= 1:
        return max(arr)

    mid = (start + end) / 2
    max1, index = find_max(arr[mid])

    if index - 1 > 0:
        top = arr[index - 1][mid]
    else:
        top = 0

    if index + 1 <= len(arr):
        bottom = arr[index + 1][mid]
    else:
        bottom = 0
    if mid - 1 > 0:
        left = arr[index][mid - 1]
    else:
        left = 0

    if mid + 1 <= len(arr):
        right = arr[index][mid + 1]
    else:
        right = 0
    present = arr[index][mid]

    print arr[mid], arr[1], max1
    if present >= top and present >= bottom and present >= left and present >= right:
        return present

    else:
        max2 = max(top, bottom, left, right)
        if top == max2:
            peakfinder(arr, start, index - 1)
        elif bottom == max2:
            if index + 1 <= len(arr):
                peakfinder(arr, index + 1, end)
            else:
                peakfinder(arr, index, end)
        elif left == max2:
            if mid - 1 > 0:
                peakfinder(arr, start, mid - 1)
            else:
                peakfinder(arr, start, mid)
        else:
            if mid + 1 < len(arr):
                peakfinder(arr, mid + 1, end)
            else:
                peakfinder(arr, mid, end)


sample_array = [
    [2, 1, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print peakfinder(sample_array, 0, 3)
