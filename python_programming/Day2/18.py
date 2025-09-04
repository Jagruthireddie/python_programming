def prime(n):
    for i in range(2,n+1):
        f=True
        for j in range(2,i):
            if i%j==0:
                f=False
                break
        if(f):
            print(i)
prime(100)