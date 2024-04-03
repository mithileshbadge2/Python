names = ['monty','vedant','nirnay']
names2 = names 
names2[0] = 'mithilesh'
print(names)
print(names2)

fruits = ['mango','banana','papaya']
fruits2 = fruits
fruits2[2] = 'apple'
print(fruits) 

cities = ['mumbai','pune','nagpur']
cities.append('bilaspur')
print(cities)

vegetables = ['cabbage','brinjal','tomato','pumpkin']
##vegetables.pop()
##print(vegetables)
# vegetables.pop(1)
# print(vegetables)
vegetables.remove('tomato')
print(vegetables)

animals = ['tiger','lion','bear','rabbit']
animals.clear()
print(animals)

animals2 = ['tiger','lion','bear','rabbit']
animals2.reverse()
print(animals2)

animals3 = ['tiger','lion','bear','rabbit','rabbit']
a1 = animals3.count('rabbit')
print(a1)

cities = ['indore','pune','nagpur','hyderabad']
cities.insert(2,'mumbai')
print(cities)

cities2 = ['indore','pune','nagpur','hyderabad']
cities2.sort()
print(cities2)

listA = [11,55,66]
listB = listA
listB[1] = 33
print(listB)





















