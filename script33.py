# reclan = 20
# with open('cities2.bin','wb') as f:
#     m = int(input("Enter the number of cities"))
#     for x in range(m):
#         city = input('enter the city')
#         city = city + (reclan - len(city)) * " "
#         city = city.encode()
#         f.write(city)

reclan = 20
with open('cities2.bin','rb')as f:
    m = int(input("record number"))
    f.seek(reclan * (m-1))
    str = f.read(reclan)
    str = str.decode()
    print(str)