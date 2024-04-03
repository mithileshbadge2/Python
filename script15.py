# list

names = ['amol','shreya','monty','harde']
# print(names)
# print(names[0])
# print(type(names))

# names.pop(2)                        #1
# print(names)
# names.remove('amol')               #2
# print(names)
names.append('vedant')                #3
print(names)
names.clear()
print(names)
numbers = [11,22,33,44,55,11]
# print(numbers)
# print(type(numbers)) 
a1 = numbers.count(11)                #4        
print(numbers[0]) 
print(a1)

animal = ['cat','lion','tiger','rabbit']
a2 = animal.index('cat')                 #5
print(a2)

animal.reverse()                        #6
print(animal)

animal.sort()                            #7
print(animal)

a1 = ['A','B',"C","D"]
a2 = ['E',"F",'G',"H"]
a1.extend(a2)                            #8
print(a1)

cities = ["mumbai",'indore','hyderabad','delhi']
cities.insert(3,'surat')                   #9
print(cities)

lst = [10,20,30]                          #10
lstB = lst.copy()
lstB[1] = 55
print(lstB)








 

