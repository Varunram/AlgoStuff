def max_heapify(x, first, last):
    largest = 2*first + 1

    while(largest <=last):
        if (last>largest) and (x[largest+1] > x[largest]):
            largest+=1

        if(x[largest] > x[first]):
            x[largest], x[first] = x[first], x[largest]
            first = largest
            largest = 2*first +1
        else:
            return

def heapsort(x):
    length = len(x) -1
    for i in range(length/2, -1, -1):
        max_heapify(x, i, length)

    for i in range(length, 0, -1):
        if (x[0] > x[i]):
            x[0], x[i] = x[i], x[0]
            max_heapify(x, 0, i-1)
            
    print x
heapsort([100,1,50,2,46,78,23,48,23])
