class bankaccount:
    def __init__(self,bal):
        self.__bal=bal
    def deposit(self,amount):
        self.amount=amount
        self.__bal=self.__bal+self.amount
    def withdraw(self,amount):
        self.amount=amount
        if self.__bal<=self.amount:
            print("Insufficient balance")
        else:
            self.__bal=self.__bal-self.amount
    def get_bal(self):
        print("Bank bal",self.__bal)
class sbi(bankaccount):
    def __init__(self, bal):
        super().__init__(bal)
    def dis(self):
        print(self.__bal)
b=bankaccount(0)
b.deposit(1000)
b.get_bal()
b.withdraw(200)
b.get_bal()
s=sbi(1200)
s.dis()