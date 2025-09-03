#Leap or not
def leap(x):
    if((x%4==0 and x%100!=0) or x%400==0):
        print("Leap year")
    else:
        print("Not a Leap year")
leap(2010)

#Character is alphabet or not
def checkchar(ch):
    if('a'<=ch<='z' or 'A'<=ch<='Z'):
        print("Alphabet")
    else:
        print("Not an alphabet")
checkchar('b')


#contains vowels and consonents
def checkvorc(c):
    if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
        print("Vowels")
    else:
        print("Consonents")
checkvorc('e')