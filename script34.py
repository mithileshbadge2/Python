# # deleting a record from file
# import os
# reclen = 20
# size = os.path.getsize('cities.bin')
# totalRecords = int(size/reclen)

# f1 = open('cities.bin','rb')
# f2 = open('cities2.bin','wb')

# deletedCity = input('Enter the city to be deleted')
# deletedCity = deletedCity + (reclen - len(deletedCity))* " "
# deletedCity = deletedCity.encode()

# for x in range(totalRecords):
#     str = f1.read(reclen)
#     if(deletedCity != str):
#         f2.write(str)
# f1.close()
# f2.close()
# os.remove('cities.bin')
# os.rename('cities2.bin','cities.bin')

# regular expression
# string
str="mithilesh:9168076805"
info = 'mithilesh-badge-29/11/1999'
print(str.split(":")[1])
print(info.split("-")[2])

