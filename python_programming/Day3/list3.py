list=[28,30,10,100,80]
l=s=list[0]
for n in list:
    if n>l:
        s=l
        l=n
    elif n>s and n!=l:
        s=n
print("Second num:",s)