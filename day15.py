birthYear  = [1990,1991,1992,1993]
ages = []

for x in birthYear:
    print(2024 - x)
    a = 2024 - x
    ages.append(a)
print(ages)

marks = [66,77,88,55,44,33,22,11]
above50 = []
for x in marks:
    if x >= 60 and x % 2 == 0:
        above50.append(x)
print(above50)

sum = [10,20,30]
total = 0
for x in sum:
    total = total + x
print(total)

cities = ['nagpur','pune','wardha']
for x in cities:
    print('welcome'+x)

