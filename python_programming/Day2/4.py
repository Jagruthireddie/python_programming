cno=int(input("Enter consumer number"))
cn=str(input("Enter consumer name"))
pmr=float(input("Enter present month reading"))
lmr=float(input("Enter last month reading"))
tu=abs(pmr-lmr)
print(tu)
if(tu>=1 and tu<=50):
    print("Current Bill:",tu*3.80)
elif(tu>50 and tu<=100):
    print("Current Bill:"(50*3.80)+(tu-50)*4.20)
elif(tu>100 and tu<=200):
    print("Current Bill:",(50*3.80)+(50*4.20)+(tu-100)*5.10)
elif(tu>200 and tu<=300):
    print("Current Bill:",(50*3.80)+(50*4.20)+(100*5.10)+(tu-200)*6.30)
else:
    print("Current Bill:",(50*3.80)+(50*4.20)+(100*5.10)+(100*6.30)+(tu-300)*7.50)

