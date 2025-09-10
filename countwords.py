def word():
    s = input("Enter string: ")
    c = 1 
    for i in s:
        if i == " ":
            c += 1
    print("Word count:", c)

word()
