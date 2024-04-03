
lst = [1969,1970,1971,1972]
ages = []
for x in lst:
    ages.append(2024-x)
print(ages)

a = [2024 - x for x in lst]
print(a)

number = [1,2,3,4,5,6,7,8,9,10]
b = [x * x for x in number]
print(b)

c = [x for x in number if x % 2 == 0]
print(c)

number = [11,12,13,14,15]
d = ["even" if x % 2 == 0 else "odd" for x in number]
print(d)

names = ['monty','vedant','mithilesh','nirnay']
e = [x for x in names if len(x) > 5]
print(e)




