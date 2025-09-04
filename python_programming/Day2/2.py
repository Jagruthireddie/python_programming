def checkchar(ch):
    if('a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
        print("Character")
    elif('0' <= ch <= '9'):
        print("Digits")
    else:
        print("Special Characters")
checkchar('$')