# names = ["chinmay","samay","vedant","mithilesh"]
# print(type(names))
# names2 = names
# names2[0] = "ram"
# print(names)
# print(names2)

# x = 100 
# print(x)
# y = x
# print(y)
# y = 500
# print(y)
# print(x) 

# numbers = [11,22,33,44,55]
# print(numbers[0])
# numbers2 = numbers
# numbers2[0] = 111
# print(numbers)
# print(numbers2)

# names = ["mahesh","suresh","nirnay"]
# names2 = names.copy()
# names2[0] ="mangesh"
# print(names)
# print(names2)

# info = {
#     "firstname": "rahul",
#     "lastname": "kumar"
# }
# info2 = info
# info2['firstname'] = 'rajesh'
# print(info)
# print(info2)

# info3 = info.copy()
# info3['lastname'] = 'more'
# print(info3)
# print(info)

cars = ["polo","bmw","mercedes",'baleno']
def addElement(lst):
    lst.append('ford')
    return lst
a = addElement(cars)
print(a)
print(cars)