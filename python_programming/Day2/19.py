def palindrome(n):
    for i in range(1,n+1):
        t=i
        s=0
        while t>0:
            r=t%10
            s=s*10+r
            t=t//10
        if s==i:
            print(i)
palindrome(100)