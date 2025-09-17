l=[20,10,70,100,50]
r=int(input("Enter index:"))
n=[]
for i in range(len(l)):
    if i!=r:
        n.append(l[i])
print("New list",n)