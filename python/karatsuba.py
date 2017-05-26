def karatsuba(num1, num2):

    if(num1/10 < 1) or (num2/10 <1 ):
        return num1*num2

    else:
        str1= str(num1)
        str2 = str(num2)
        l1 = max(len(str1), len(str2))
        x = int(l1)/2
        x1 = 10**x

        a = num1/x1
        c = num2/x1
        d = num2%x1
        b = num1%x1

        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ad_bc= karatsuba(a+b, c+d) - a*c - b*d
        product = 10**(2*x)*ac + (x1)*(ad_bc) + bd

        return product

print karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)
