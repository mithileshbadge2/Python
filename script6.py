x = 10
print(x)

names = ["mithilesh","vedant","nirnay","monty"]
print(names)
names[2] = "shishir"
print(names)

city = ["nagpur","pune","bangalore","hyderabad"]
print(city[2])

fruits = ["mango","banana","grapes","papaya"]
print(len(fruits))

#update value in list
animals = ["tiger","lion","cat","rabbit"]
animals[0] = "jaguar"
print(animals)

country = ["india","nepal","china","pakistan","srilanka"]
for x in range(5):
    #print(x)
    print(country[x])

# For loop
country = ["india","nepal","china","pakistan","srilanka"]
for x in range(len(country)-1,-1,-1):
    #print(x)
    print(country[x])

#while loop
flowers = ["lily","rose","jasmine","sunflower"]
#print(flowers)
i1 = 0
while(i1 < len(flowers)):
    #print(i1)
    print(flowers[i1])
    i1 = i1 + 1

i2 = len(flowers) -1
while(i2 >= 0):
    #print(i2)
    print(flowers[i2])
    i2 = i2 -1

names = ["mithilesh","rohit","monty","nirnay",'vedant']
print("monty" in names)

