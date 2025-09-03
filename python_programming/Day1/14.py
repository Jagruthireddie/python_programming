#COntrol Statements
#conditional

#if
a=10
b=5
if a>b:
    print("A is greater")
print("tq")

#if-else
a=10
b=20
if a>b:
    print("A is greater")
else:
    print("B is greater")
    
    
def evenorodd(x):
    if x%2==0:
        print("Even")
    else:
        print("Odd")
evenorodd(1)

def posorneg(y):
    if(y>0):
        print("Positive")
    elif(y<0):
        print("Negative")
    else:
        print("Zero")
posorneg(-10)


def divsible(z):
    if(z%5==0 and z%11==0):
        print("Number is divisible by 5 and 11")
    else:
        print("Not divisible")
divsible(55)

