def string():
    s=input("Enter string:")
    c=0
    for i in s:
        c+=1
    print(c)
    s1=input("Enter string2:")
    if s==s1:
        print("equal")
    else:
        print("not equal")
    print(s+"Good Morning")
string()