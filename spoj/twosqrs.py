import numpy
import math

def square(num):
    lower = int(math.floor(math.sqrt(num)))
    return (lower*lower == num)

def check(num):
    lower = int(math.floor(math.sqrt(num)))
    for i in xrange(lower+1):
        if square(num-i*i):
            print 'Yes'
            return
    print 'No'

n = int(raw_input())
for rand in xrange(n):
    check(int(raw_input()))
