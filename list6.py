l=[1,2,3,4,1,1,4,2]
l1=[]
l2=[]
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i]==l[j]:
            c+=1
    l2.append(c)
    if c==1:
        l1.append(l[i])
print(l1)
print("Freq",l2)