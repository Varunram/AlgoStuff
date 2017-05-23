n = raw_input()
n1 = int(n)
if (n1<10):
    print 1

else:
    pwr = 10 ** (len(n) -1)
    print (pwr - n1%pwr)
