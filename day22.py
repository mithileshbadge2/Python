# int as param and inter as a return type
def add(x,y):
    return x + y
a = add(12,3)
print(a)


# float 
# float as a parameter and float as return type 
def add(x,y):
    return x + y
b = add(45.9,7.3)
print(b)

# string 
# string as parameter and string as return 
def greet(name):
    return "hi "+name
c  = greet("mithilesh")
print(c)

#boolean 
#boolean as parameter and boolean as return type 
def canDrive(above18):
    if  above18:
        return True
    else:
        False
d = canDrive(True)
if(d):
    print("Allowed to drive!")
else:
    print("Not allowed to drive")
    

# list
#list as parameter and list as return type 
city = ["pune","mumbai","banglore","kolkata"]
def addCity(lst):
    lst.append("wardha")
    return lst
e = addCity(city)
print(e)
print(city)


# dict
# dict as parameter and dictionary as return type 

dict = {
    "firstName":"mithilesh",
    "lastName":"badge"
}

def addCityToInfo(info):
    info['city'] = "pune"
    return info
f = addCityToInfo(dict)
print(f)

# tuple as parameter and tuple as return type 
def addNum(tupA):
    tupA = list(tupA)
    tupA.append(555)
    tupA = tuple(tupA)
    return tupA
a,b,c = addNum((2,3))
print(a)
print(b)
print(canDrive)
# set as parameter and set as return type 
setA = {11,12,13}
def addToSetA(ss):
    ss.add(44)
    return ss
f = addToSetA(setA)
print(setA)