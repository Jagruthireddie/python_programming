def ecomm():
    l=[]
    while(True):
        print("1.Add")
        print("2.Remove")
        print("3.Search")
        print("4.Display")
        print("5.total")
        print("6.sort")
        print("7.clear")
        r=int(input("Enter the choice:"))
        if(r==1):
            l.append(input())
        elif(r==2):
            r1=input("Enter:")
            if r1 in l:
                print(l.remove(r1))
            else:
                print("Error")
        elif(r==3):
            k=input("Enter the value:")
            if k in l:
                print("Found")
            else:
                print("Not found")
        elif(r==4):
            print(l)
        elif(r==5):
            print(len(l))
        elif(r==6):
            print(l.sort())
        elif(r==7):
            l.clear()
            print(l)
        else:
            print("Error")
ecomm()