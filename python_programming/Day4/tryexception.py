def exception():
    x=int(input("Enter no1"))
    y=int(input("Enter no2"))
    try:
        z=x/y
        print(z)
    except:
        print("Cannot divide by zero")
    finally:
        print(x,y)
exception()
