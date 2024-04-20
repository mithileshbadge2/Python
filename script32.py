# reclan = 20
# with open('cities.bin','wb') as f:
#     n = int(input('Enter the number of cities'))
#     for x in range(n):
#         city = input('enter the city')
#         city = city + (reclan - len(city)) * " "
#         city = city.encode()
#         f.write(city)

# p2
reclan = 20
with open('cities.bin','rb') as f:
    m = int(input("record number"))
    f.seek(reclan * (m-1))
    str = f.read(reclan)
    str = str.decode()
    print(str)


