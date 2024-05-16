# reclan = 20
# with open('cities2.bin','wb') as f:
#     m = int(input("Enter the number of cities"))
#     for x in range(m):
#         city = input('enter the city')
#         city = city + (reclan - len(city)) * " "
#         city = city.encode()
#         f.write(city)

# reclan = 20
# with open('cities2.bin','rb')as f:
#     m = int(input("record number"))
#     f.seek(reclan * (m-1))
#     str = f.read(reclan)
#     str = str.decode()
#     print(str)

# import os
# reclan = 20
# size = os.path.getsize('cities2.bin')
# totalRecords = int(size/reclan)

# with open('cities2.bin','rb') as f:
#     city = input('enter the city')
#     city = city + (reclan - len(city))*" "
#     city = city.encode()
#     position = 0
#     found = False
#     for x in range(totalRecords):
#         f.seek(position)
#         acity = f.read(reclan)
#         if city in acity:
#             print('city found')
#             found = True
#             break
#         position = position + reclan
#     if not found:
#         print("city not found")


import os
reclan = 20
size = os.path.getsize('cities2.bin')
totalRecords = int(size/reclan)

with open('cities2.bin','r+b') as f:
    rep = input('enter the city to replace')
    rep = rep + (reclan - len(rep)) * " "
    rep = rep.encode()
    update = input('enter city to replace with')
    update = update + (reclan - len(update)) * " "
    update = update.encode()

    position = 0
    found = False
    for x in range(totalRecords):
        f.seek(position)
        ac = f.read(reclan)
        if ac == rep:
            found = True
            f.seek(-20,1)
            f.write(update)
            break
        position = position + update
    if not found:
        print('city not found')
