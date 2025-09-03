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