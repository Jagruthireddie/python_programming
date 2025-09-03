#function with parameters and return type
def add(a,b):
    c=a+b
    return c
x=10
y=20
z=add(x,y)
print(z)


def conversion(d):
    y=d/365
    m=d/30
    return y,m
d1=365
z1=conversion(d1)
print(z1)