from collections import Counter
while (1):
    x = raw_input()
    if x=='*':
        break
    x = Counter(x).most_common()
    print x[0][1]
