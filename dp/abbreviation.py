def comp(arr, g):
    i =0
    while arr and g:
        if str(arr[0]).upper() == g[0]:
            g = g[1:]
            arr = arr[1:]
        elif ord(arr[i]) >97:
            arr = arr[1:]
        else:
            return False
    if g:
        return False
    else:
        for i in range(len(arr)):
            if ord(arr[i]) < 90:
                return False
        return True



n = int(raw_input())

for _ in range(n):
    str1 = raw_input()
    str2 = raw_input()
    if(comp(str1, str2)):
        print "YES"
    else:
        print "NO"
