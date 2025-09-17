#library management system
def dict():
    d={}
    while True:
        print("1.Add")
        print("2.Remove")
        print("3.Search")
        print("4.update")
        print("5.Display")
        print("6.count")
        print("7.title")
        c=int(input("enter the choice"))
        if(c==1):
            k=input("enter the key ")
            v=input("enter the value")
            if k in d:
                print(k,"already exists")
            else:
                d[k]=v
        elif(c==2):
            k=input("enter the key ")
            if k in d:
                d.pop(k)
            else:
                print(k,"doesn't exist")
        elif c==3:
            k=input("enter the key ")
            if k in d:
                print("book is found",d[k])
            else:
                print("book not found")
        elif c==4:
            k=input("enter the key ")
            if k in d:
                d[k]=input("enter new title")
                print("book updated")
            else:
                print("book not found")
        elif c==5:
            print(d)
        elif c==6:
            print("total no of books:",len(d))
        elif (c==7):
            v=input("enter the book title")
            if v in d.values():
                print("book exists")
            else:
                print("book doesn't exist")
        else:
            exit()
dict()