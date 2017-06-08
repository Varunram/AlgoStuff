def mfibo(one,two,n):
    if n==1:
        return one
    if n ==2:
        return two
    else:
        for i in range(3,n+1,1):
            three = one + two*two
            one = two
            two = three
        return two

one, two, n = map(int, raw_input().split())
print mfibo(one,two,n)
