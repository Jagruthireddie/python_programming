l=[1,2,3,4,5,6,7,8,9]
c=0
c1=0
for i in l:
    if i%2==0:
        c+=1
    else:
        c1+=1
print("Even num:",c)
print("Odd num:",c1)