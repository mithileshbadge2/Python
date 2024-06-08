students = [
    {
        "firstName":"Mithilesh",
        "lastName":"Badge",
        "age":24,
        "rollNo":38,
        "skills":["css","html","js"]
    },
    {
        "firstName":"Vedant",
        "lastName":"Gaikwad",
        "age":23,
        "rollNo":40,
        "skills":["css","html","js","sql"]
    },
    {
        "firstName":"Snehal",
        "lastName":"Kamble",
        "age":25,
        "rollNo":35,
        "skills":["css","html","js","sql",'mongoDB']
    }
]
# print(students[0])
print(students[0]['firstName'] +" "+ students[0]['lastName'])

for x in students:
    print(x['firstName'] + " " + x['lastName'])

for x in students:
    print(x['firstName'] + ":" + str(len(x["skills"])))

total = 0
for x in students:
    total = total + x['age']
print(total/len(students))

for x in students:
    x['skills'].append("reactjs")
print(students)

for x in students:
    x["country"] = "India"
print(students)

for x in students:
    if(x["age"] >= 24):
        print(x["firstName"])

