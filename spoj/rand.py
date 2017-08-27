def palindrome(num):
    str1 = [int(d) for d in str(num)]
    if(len(str1)%2==0):
        str1[len(str1)/2-1]+=1
        rev = str1[:len(str1)/2]
        str1=rev+rev[::-1]

    else:
        str1[len(str1)/2]+=1
    return "".join(map(str, str1)

palindrome(1122)
