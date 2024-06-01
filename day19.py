# cities = ['nagpur','pune','goa','kanpur']
# print(cities)
# print(type(cities))

names = ('ramesh','suresh')
print(type(names))
names = "goa",
print(type(names))

cities = ['nagpur','pune','goa','kanpur']
# for x in range(len(cities)):
#     print(cities[x])

# for x in cities:
#     print(x)

i1 = 0
while(i1 < len(cities)):
    print(cities[i1])
    i1 = i1 + 1

cars = ('bmw','mercedes','tata','hyundai','polo','suzuki','verna')
a,b,c,d,e,f,g = cars
print(d)

money = ['rupees','dollar','pounds']
def addmoney(lst):
    lst.append("euro")
    return tuple(lst)

a,b,c,d = addmoney(money)
print(d)

n = (10,20,30,40)
m = list(n)
m.append(40)
o = tuple(m)
print(o)

a = o.count(40)
print(a)
b = o.index(10)
print(b)
