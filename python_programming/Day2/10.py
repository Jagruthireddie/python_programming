def prime(n):
    if n<1:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
k=7
if(prime(k)):
    print(k,"Prime number")
else:
    print(k,"not prime number")