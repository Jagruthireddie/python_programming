cno=int(input("Enter consumer number"))
cn=str(input("Enter consumer name"))
pmr=float(input("Enter present month reading"))
lmr=float(input("Enter last month reading"))
tu=abs(pmr-lmr)
print(tu)
cb=tu*3.80
print(cb)
print("Consumer number=",cno,"Consumer Name=",cn,"present month reading=",pmr,"Last month reading=",lmr,"Total units=",tu,"Current bill=",cb)