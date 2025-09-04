def digitscount(n):
    c=0
    while n>0:
        r=n%10
        c=c+1
        n=n//10
    print(c)
digitscount(234)
        