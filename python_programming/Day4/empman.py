class employee:
    def __init__(self,ename,esal):
        self.ename=ename
        self.esal=esal
    def display(self):
        print("Emp name",self.ename)
        print("Emp sal",self.esal)
class manager(employee):
    def __init__(self,ename,esal,dept):
        super().__init__(ename,esal)
        self.dept=dept
    def display(self):
        super().display()
        print("Dept",self.dept)
e=employee("jagu",60000)
e.display()
m=manager("laha",80000,"cse")
m.display()
        