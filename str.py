def check():
    s=input("Enter string")
    c=0
    c1=0
    c2=0
    for i in s:
        if 'a'<=i<='z'or 'A'<=i<='Z':
            c+=1
        elif '0'<=i<='9':
            c1+=1
        else:
            c2+=1
    print(c)
    print(c1)
    print(c2)
check()