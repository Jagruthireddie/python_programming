def occur():
    s=input("Enter string")
    c=input("Enter the occurrence ")
    l=[]
    for i in range(len(s)):
        if s[i]==c:
            l.append(i)
    print(l)
occur()