# setA = {10,20,30}
# setA.add(40)
# print(setA)

# setB = setA.copy()
# setB.add(35)
# print(setB)

# setA = {10,20,30,40}
# setA.pop()
# setA.remove(30)
# print(setA)

# setA = {25,50,75}
# setB = {100,150,200}
# setC = setB.union(setA)
# print(setC)

# setM = {10,20,30}
# setN = {30,15,10}
# setP = setM.intersection(setN)
# print(setP)

# set1 = {6,77,88}
# set2 = {55,68,77}
# set3 = set2.difference(set1)
# print(set3)
# print(set1)
# print(set2)

# set1.difference_update(set2)
# print(set1)

set12 = {66,77,88}
set22 = {55,68,77}
set12.intersection(set22)
set12.intersection_update(set22)
print(set12)

setX = {50,100,150}
setY = {25,50,75}
setZ = setX.symmetric_difference(setY)
print(setZ)

setX.symmetric_difference_update(setY)
print(setX)


setA = {11,22,33}
setB = {11,22}

a = setB.issubset(setA)
b = setA.issuperset(setB)
print(a)
print(b)

setX = {11,22,33,44}
setY = {11,223,335,446}  
c = setX.isdisjoint(setY)
print(c)
