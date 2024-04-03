info3 = {
    "firstName" : 'monty',
    "lastName" : "badge",
    "age" : 23,
    "rollno" : 38
}
print(info3)
print(info3["firstName"])
print(info3['age'])
print(info3.get('lastName'))

y = info3.setdefault('city',"pune")
print(y)
print(info3)

##info4 = dict.fromkeys(["keyone","keytwo","keythree"])
#print(info4)

students = [
    {
        'firstName' : "monty",
        'lastName' : 'badge',
        'age' : 23,
        'skills' : ['html','css','js']
    },
    {
        'firstName' : "vedant",
        'lastName' : "gaikwad",
        'age' : 24,
        "skills" : ["html","css","python"]

    },
    {
        'firstName' : "nirnay",
        'lastName' : "bhau",
        'age' : 25,
        'skills' : ['html',"css","js","python"]

    }

]

print(students[2]['firstName'])
print(students[1]["skills"])
print(students[0]["age"])

for x in students:
    print(x['age'])

for x in students:
    #print(x['skills'])
    #if "python" in x['skills']:
        #print(x["firstName"])
    #if "bhau" in x["lastName"]:
        #print(x["firstName"])
    #if "monty" in x["firstName"]:
        #print(x["firstName"])
    #if "html" in x['skills']:
        #print(x["age"])
    if "gaikwad" in x['lastName']:
        print(x["age"])



for x in students:
    if x['age'] > 20 and "python" in x['skills']:
        print(x['firstName'],x['age'],x["skills"])

for x in students:
    if x["age"] > 20 and "vedant" in x["firstName"]:
        print(x["skills"],x["age"],x["lastName"])


for x in students: #no. of skills
    print(x['firstName']+":"+ str(len(x['skills'])))
    print(x['lastName']+":"+ str(len(x['skills'])))

total = 0
for x in students:
    total = total + x['age']
    print(total/len(students))





















