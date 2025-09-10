def count():
    s=input("Enter string")
    l=[]
    for c in s:
        if c not in l:
            ch=0
            for c1 in s:
                if c==c1:
                    ch+=1
            print(f"{c}{ch}",end="")
            l.append(c)
count()