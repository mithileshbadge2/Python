# set
names = ["mithilesh","vedant","ram","rhiday","pawan"]
print(names)

names = {"mithilesh","vedant","ram","rhiday","pawan"}
print(names)


# program 2
names2 = ["mithilesh","vedant","ram","rhiday","pawan"]
print(names2[2])
names2 = {"mithilesh","vedant","ram","rhiday","pawan"}
#print(names2[2])

# program 3
for item in names2:
    print(item)

# program 4
print("vedant" in names2)

a = "mithilesh"
b = ("shobhit","nirnay")
c = ["subhuti","sayali"]
d = {
    "firstName":"mithilesh",
    "lastName":"badge"
}
e = {"rohan","kunal"}

print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))

listA = [11,22,33]
print(max(listA))
print(min(listA))

del a
del b
del c
del d
del e


# set 

number = {11,22,3,3,4,44,55}
number.add(666)
print(number)

# number.clear()
# print(number)

number.pop()
print(number)

number.remove(666)
print(number)

setA = {11,22,33}
# setB = setA
# setB.remove(22)

# print(setA)
# print(setB)
setB = setA.copy()
print(setB)
setB.remove(22)
print(setA)
print(setB)