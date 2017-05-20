from collections import Counter
while (1):
    x = raw_input()
    length = len(x)
    if x=='*':
        break
    x = Counter(x).most_common()
    for i in x:
        if(length%i[1]==0):
            print i[1]
            break
