def check():
    s=input("Enter string")
    c=0
    c1=0
    if s.isalpha():
        for i in s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                c+=1
            else:
                c1+=1
    else:
        print("Invalid")
    print(c)
    print(c1)
check()