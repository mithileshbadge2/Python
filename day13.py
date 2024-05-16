# firstName = "monty"
# lastName = 'badge'
# info = '''
# my name is monty 
# '''
# info = """
# my name is monty
# """ 

# team = 'India'
# print(team[0])

# team[0] = 'i'
# print(team)

# ipl = 'chennai'
# print('c' in ipl)
# print('C' in ipl)

# for x in range(7):
#     # print(x)
#     print(ipl[x])

# for x in ipl:
#     print(x)

# i1 = 0
# while(i1 < len(ipl)):
#     print(ipl[i1])
#     i1 = i1 + 1

# string methods
team = 'Bangalore'
a = len(team)
print(a)

veg = 'brinjal'
b = veg.upper()
print(b)

game = 'GTA5'
c = game.lower()
print(c)

first_name = 'mithilesh'
d = first_name.capitalize()
print(d)

last_name = 'badge'
e = last_name.startswith("ba")
print(e)

phone_number = '8329098875'
f = phone_number.endswith('75')
print(f)

city = 'nagpur'
g = city.replace('nagpur',"wardha")
print(g)

address = ['monty','badge',"9168076805"]
h = '/'.join(address)
print(h)


