def digit(n):
    t=n%10
    while n!=0:
        r=n%10
        n=n//10
    print(r)
    print(t)
    print(r+t)
    
digit(123456)