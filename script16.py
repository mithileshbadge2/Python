# int as par
# int as ret ty

def addOne(x,y):
    return x + y
e = addOne(12,5)
print(e)

def subOne(x,y):
    return x - y
e2 = subOne(15,2)
print(e2)

# float as par
# float as ret ty

def subOne(x,y):
    return x - y
e3 = subOne(5.3,6.2)
print(e3)

# bol as p&r

def canDrive(age,haveVehicle):
    if age > 18 and haveVehicle:
        return True
    else:
        return False
e4 = canDrive(19,True)
print(e4)

# string as P&R

def greet(name):
    return("welcome "+name)
e5 = greet("monty !")
print(e5)

# list as P&R

names = ['mithilesh','vedant','nirnay']
def addName(lst):
    lst.append('ajay')
    return lst
e6 = addName(names)
print(e6)

# dic as P&R
info = {
    "firstName":"monty",
    "lastName":"badge"
}
def addCity(information):
    information['city'] = "nagpur"
    return information
e7 = addCity(info)
print(e7)

# tuple as P&R
numbers = (1,2,3,4)
def addValue(tupA):
    tupA = list(tupA)
    tupA.append(44)
    tupA = tuple(tupA)
    return tupA
e8 = addValue(numbers)
print(e8)

# set as P&R
setA = {10,20,30}
def addElement(seta):
    seta.add(40)
    return seta
e9 = addElement(setA)
print(e9)










