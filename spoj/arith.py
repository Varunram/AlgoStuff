#Ugly Code Warning!!!
import os
n = raw_input()
if "+" in n:
    n1,n2 = n.split('+')
    n2x = "+"+n2
    res = int(n1)+int(n2)
if "-" in n:
    n1,n2 = n.split("-")
    n2x = "-"+n2
    res = int(n1)-int(n2)


if "*" in n:
    n1,n2 = n.split("*")
    res=str(int(n1)*int(n2))
    n2x = "*"+n2
    n2 = list(n2)
    i1 = len(res) - (len(str(int(n1)*int(n2[0]))))
    i = i1
    print " "*(len(res) - len(str(n1)))+ n1
    print " "*(len(res) - len(str(n2x))) +n2x
    print " "*(len(res) - (max(len(n1), len(n2x)) )) + "-"*(max(len(n1), len(n2x)))
    while(n2):
        if(int(n2[-1])!=0):
            print i*" "+str(int(n1)*int(n2[-1]))
        else:
            print (len(res)-(i1-i)-1)*" "+"0"
        del n2[-1]
        i-=1
    if(len(res) != len(n1) and len(res)!= len(n2)):
        print "-"*len(res)
        print res
    os._exit(1)


diff = len(n1) - len(n2x)
if(len(n1) > len(n2)):
    n2x = " "*diff + str(n2x)
    n1x = n1
else:
    n1x = " "*(-diff) + str(n1)

print '\n'
print n1x
print n2x
x = max(len(n1x), len(n2x))
print "-"*(x)
y = str(res)
print " "*(x - len(y)) + y
