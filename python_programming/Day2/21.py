def strong(n):
    for i in range(1, n+1):
        t = i
        a = 0
        while t > 0:
            r = t % 10
            s = 1
            for j in range(1, r+1):
                s *= j
            a += s
            t //= 10
        if i == a:
            print(i)

strong(1000)
