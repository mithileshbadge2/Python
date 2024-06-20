birthYear = [1989,1990,1991,1992]
ages = []
for x in birthYear:
    ages.append(2024-x)
print(ages)

[2024-x for x in birthYear]

a = list(map(lambda x : 2024-x,birthYear))
print(a)

marks = [89,90,91,34,56]
above50 = []
for x in marks:
    if x > 50:
        above50.append(x)
print(above50)

lst = [10,20,30,40]
total = 0
for m in lst:
    total = total + m
print(total)

from functools import *
lst = [1,2,3,4,5]
h = reduce(lambda x,y:x+y,lst)
print(h)

lst2 = [11,22,33]
print(sum(lst2))
print(max(lst2))
print(min(lst2))


e = [total := total + x for x in lst]
print(e)




