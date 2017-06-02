def count(length):
    global COUNT
    COUNT = COUNT + length

def merge(a,b):
    c=[]
    while len(a)!=0 and len(b)!=0:
        if(a[0]<b[0]):
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            count(len(a))
            b.remove(b[0])

    c+=b if len(a)==0 else a
    return c

def mergesort(x):
    if(len(x)<2):
        return x
    else:
        middle = len(x)/2
        a = mergesort(x[:middle])
        b= mergesort(x[middle:])
        return merge(a,b)

COUNT =0
lines = tuple(open('test.txt', 'r'))
res = []

for line in lines:
    res.append(int(line.strip('\n')))

print res
print mergesort(res)
print COUNT
