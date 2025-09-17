class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
            print("Name",self.name)
            print("Rollno",self.roll)
            print("marks",self.marks)
s1=student("Jagu",516,90)
s1.display()
s2=student("Yashu",563,95)
s2.display()