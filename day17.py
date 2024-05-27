info = {
    "firstName":"Mithilesh",
    "lastName":"Badge",
    "age":24,
    "Rollno":38
}
print(info["firstName"])
info["Rollno"] = 35
print(info)
info["city"] = "Nagpur"
print(info)
info.pop('lastName')
print(info)
info.popitem()
print(info)
print("Rollno" in info)

# Person = {
#     'name':'monty',
#     'age': 30,
#     'height' : 6,
#     'body' : "slim"
# }
# for x in Person:
#     print(x,Person[x])

Person = {
    'name':'monty',
    'age': 30,
    'height' : 6,
    'body' : "slim"
}

for x in Person.keys():
    print(x)

for y in Person.values():
    print(y)

for x,y in Person.items():
    print(x,y)


vehicle = {
    "color" : "blue",
    "type" : 'sedan',
    "Regno" : "555"
}

print(vehicle["color"])
a = vehicle.get('color')
print(a)

vehicle.pop('type')
print(vehicle)

vehicle.clear()
print(vehicle)

dictOne = {"5":"five","6":"Six"}
dictTwo = {"7": "seven","8":"Eigth"}
dictTwo.update(dictOne)
print(dictTwo)

info2 = {
    "firstName":"amol",
    "lastName":"rao",
    "age":33,
    "city":"nagpur"
}
info2.setdefault("city","mumbai")
print(info2)

c = dict.fromkeys(["four","five","six"])
print(c)

