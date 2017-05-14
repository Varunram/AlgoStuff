def merge(a,b):
    c=[]
    while len(a)!=0 and len(b)!=0:
        if(a[0]<b[0]):
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
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

print mergesort([99,95,32,45,64,1,2,3,4])
