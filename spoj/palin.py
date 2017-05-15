def pal_gen(low,upp):
    palindromes =[]
    low1=int(low)+1
    i =0
    while(i<=upp):
        if(str(low1) == str(low1)[::-1]):
            palindromes.append(low1)
            break
        i+=1
        low1+=1
    print palindromes[0]

i=0
while(i<raw_input()):
    x = raw_input()
    if(len(x) ==1):
        print i+1
    if(len(x)==2):
        pal_gen(x, 10)
    else:
        pal_gen(x, 10**(len(x)-2))
    i+=1
