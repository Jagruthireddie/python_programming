from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, plate, owner):
        self.__plate = plate
        self.__owner = owner
    def get_plate(self): 
        return self.__plate
    def set_plate(self, p): 
        self.__plate = p
    def get_owner(self): 
        return self.__owner
    def set_owner(self, o): 
        self.__owner = o
    @abstractmethod
    def display(self): 
        pass
    @abstractmethod
    def fee(self,h): 
        pass

class Bike(Vehicle):
    def __init__(self,plate,owner,helmet=True):
        super().__init__(plate,owner); 
        self.__helmet=helmet
    def get_helmet(self): 
        return self.__helmet
    def display(self): 
        print("Bike",self.get_plate(),self.get_owner(),self.get_helmet())
    def fee(self,h): 
        return 20*h

class Car(Vehicle):
    def __init__(self,plate,owner,seats=4):
        super().__init__(plate,owner); 
        self.__seats=seats
    def get_seats(self): 
        return self.__seats
    def display(self): 
        print("Car",self.get_plate(),self.get_owner(),self.get_seats())
    def fee(self,h): 
        return 50*h

class Truck(Vehicle):
    def __init__(self,plate,owner,max_load=1000):
        super().__init__(plate,owner); 
        self.__max_load=max_load
    def get_max_load(self): 
        return self.__max_load
    def display(self): 
        print("Truck",self.get_plate(),self.get_owner(),self.get_max_load())
    def fee(self,h): 
        return 100*h

class ParkingSpot:
    rank={'S':1,'M':2,'L':3,'XL':4}
    def __init__(self,sid,size):
        self.sid=sid;self.size=size;self.__vehicle=None
    def is_free(self):
        return self.__vehicle is None
    def fits(self,v):
        need={'Bike':'S','Car':'M','Truck':'XL'}[v.__class__.__name__]
        return ParkingSpot.rank[self.size]>=ParkingSpot.rank[need]
    def park(self,v):
        if self.is_free() and self.fits(v):
            self.__vehicle=v;
        print("Parked",v.get_plate(),"at",self.sid)
    def unpark(self):
        v=self.__vehicle;
        self.__vehicle=None
        if v:
            print("Unparked",v.get_plate(),"from",self.sid)
        return v
    def show(self):
        print("Spot",self.sid,self.size,"Free" if self.is_free() else "Occupied")

class ParkingLot:
    def __init__(self):
        self.spots=[]
    def add_spot(self,s):
        self.spots.append(s)
    def show_spots(self):
        [s.show() for s in self.spots]
    def park_vehicle(self,v):
        for s in self.spots:
            if s.is_free()and s.fits(v):
                s.park(v);return
        print("No spot for",v.get_plate())
    def unpark_vehicle(self,v,h):
        for s in self.spots:
            if not s.is_free()and s._ParkingSpot__vehicle==v:
                s.unpark();fee=v.fee(h);print("Fee",fee);return fee

class Payment(ABC):
    @abstractmethod
    def pay(self,a):
        pass

class CashPayment(Payment):
    def pay(self,a):
        print("Paid ₹",a,"cash")

class UPIPayment(Payment):
    def pay(self,a):
        print("Paid ₹",a,"UPI")

bike=Bike("B1","jagu")
car=Car("C1","laha")
truck=Truck("T1","ma",8000)
for v in [bike,car,truck]:
    v.display()
lot=ParkingLot()
lot.add_spot(ParkingSpot(1,'S'))
lot.add_spot(ParkingSpot(2,'M'))
lot.add_spot(ParkingSpot(3,'XL'))
lot.show_spots()
lot.park_vehicle(bike)
lot.park_vehicle(car)
lot.park_vehicle(truck)
lot.show_spots()
fee=lot.unpark_vehicle(car,2)
if fee:
    UPIPayment().pay(fee)
lot.show_spots()
try:
    print(bike.__plate)
except:
    print("Direct access failed")
print("Via getter:",bike.get_plate())
