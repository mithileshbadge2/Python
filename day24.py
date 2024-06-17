birthYear = [1989,1990,2000, 2001]
ages = []
for i in birthYear:
    e = 2024-i
    ages.append(e)
print(ages)

# list comprehension
f = [2024 - i for i in birthYear ]
print(f)

marks = [22,44,55,22,33,55,66]
above50 = []
for i in marks:
    if(i > 50):
        above50.append(i)
print(above50)

# list comprehension
e = [i for i in marks if i > 50]
print(e)

listE = [45,66,33,44,56]
oddEven = []
for i in listE:
    if i % 2 == 0:
        oddEven.append("even")
    else:
        oddEven.append("odd")
print(oddEven)

f = ["even" if i % 2== 0 else "odd" for i in listE]
print(f)

x = [1,2,3,4,5,6,7,8,9,10]
x2 = [i * 2 for i in x]
print(x2)