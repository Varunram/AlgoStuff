def process(r1, r2, min1, max1):
    minx= maxx =0
    for i in range(len(min1)):
        if min1[i]<r1 and max1[i]<r2 and max1[i]>r1:
            maxx+=1
            continue
        if min1[i]<r1 and max1[i]>r2 and max1[i]>r1:
            maxx+=1
            continue
        if min1[i]>r1 and min1[i]<r2 and max1[i]<r2:
            minx+=1
            maxx+=1
            continue
        if (min1[i] == r1 and max1[i]!=r2) or (max1[i] == r2 and min1[i]!=r1):
            maxx+=1
    print ('%d %d' %(minx, maxx))


r1,r2 = map(int, raw_input().split())
n=  int(raw_input())
min1 =[]
max1=[]
for i in range(n):
    min1x, max1y = map(int, raw_input().split())
    min1.append(min1x)
    max1.append(max1y)

process(r1,r2,min1,max1)
