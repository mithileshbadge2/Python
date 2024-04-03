lst = [1999,2000,2001,2002]
ages = []

for l in lst:
    x = 2024 - l
    ages.append(x)
print(ages)

a = list(map(lambda x:2024-x,lst))
print(a)

print([2024 - l for l in lst])

lstA = [10,20,30,40]
numbers = []
for n in lstA:
    x = 50-n
    numbers.append(x)
print(numbers)

c = list(map(lambda x: 50 - x,lstA))
print(c)

print([50 - n for n in lstA])

lstB = [1969,1970,1971,1972]
age = []
for a in lstB:
    x = 2024 - a
    age.append(x)
print(age)
d = list(map(lambda x: 2024 - x,lstB))
print(d)
print([2024 - a for a in lstB])

names = ['akash','ninad','rakesh','shubham']
above5 = []
for x in names:
    if len(x) > 5:
        above5.append(x)
print(above5)

print([x for x in names if len(x) > 5 ])

e = list(filter(lambda x : len(x) > 5,names))
print(e)

transactions = []
d = [5,10,15,-20,-36,-52,555]
for x in d:
    if x < 0:
        # print('withdrawal')
        transactions.append('withdraw')
    else:
        transactions.append('deposit')
print(transactions)
print(['withdrawl' if x < 0 else 'deposit' for x in d])
print(list(filter(lambda x: x > 0,d)))
print(list(filter(lambda x: x < 0,d)))


