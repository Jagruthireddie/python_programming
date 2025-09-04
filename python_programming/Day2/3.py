sid=int(input("Enter student number"))
name=str(input("Enter student name"))
s1=int(input("Enter maths marks"))
s2=int(input("Enter physics nmarks"))
s3=int(input("Enter chemistry marks"))
t=s1+s2+s3
print(t)
avg=t/3
print(round(avg,2))
print("Student number=",sid,"Student name=",name,"Student marks=",s1,s2,s3,sep=',')
if(avg>=40):
    print("Pass")
    if(avg>40 and avg<=50):
        print("Grade C")
    elif(avg>50 and avg<=70):
        print("Grade B")
    elif(avg>70 and avg<=80):
        print("Grade A")
    elif(avg>80 and avg<=100):
        print("Destination")
    else:
        print("Error")
else:
    print("Fail")
