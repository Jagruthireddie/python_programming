def words(x):
    digits=str(x)
    for d in digits:
        if d=='1':
            print("One")
        elif d=='2':
            print("Two")
        elif d=='3':
            print("Three")
        elif d=='4':
            print("Four")
        elif d=='5':
            print("Five")
        elif d=='6':
            print("Six")
        elif d=='7':
            print("Seven")
        elif d=='8':
            print("Eight")
        elif d=='9':
            print("Nine")
        else:
            print()
words(12399)