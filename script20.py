class PersonB:
    # constructor
    def __init__(self,fn,ln):
        self.first_name  = fn 
        self.last_name = ln 

    def talk(self):
        print("I am talking")
    
    def walk(self):
        print("I am walking")

amol = PersonB("amol","rao")
chinmay = PersonB("chinmay","deshpande")

print(amol.first_name)
print(amol.last_name)

print(chinmay.first_name)
print(chinmay.last_name)
chinmay.city = "pune"
print(chinmay.city)
# print(amol.city)

class Vehicle:
    def __init__(self,vt,m):
        self.vehicle_type = vt
        self.model = m
    def start(self):
        print("I am starting")
    def stop(self):
        print("I am stopping")

car = Vehicle("car", "Maruti")
bike = Vehicle('bike',"Ninja")

print(car.vehicle_type)
print(car.model)

print(bike.vehicle_type)
print(bike.model)
