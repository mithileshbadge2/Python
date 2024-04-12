# create obj
# f = open('myfile.txt','w')
# # take user input
# str = input('Enter the name')
# # write to file
# f.write(str)
# # close the file
# f.close()

# f = None
# try:
#     fileName = input('Enter the name')
#     f = open(fileName,'r')
#     str = f.read()
#     print(str)
# except FileNotFoundError:
#     print("File not found")
# finally:
#     if f is not None:
#         f.close()
# print("bye")

# p1
# open the file
# f = open('myfile.txt','w')
# # # take input from user
# name = input('enter the name')
# # # write the file
# f.write(name)
# # # close
# f.close()

# p2
# fileName = input("enter the name")
# f = open(fileName,'r')
# str = f.read()
# print(str)
# f.close()

# p3

# f = None
# try:
#     fileName = input("Enter the fileName")
#     f = open(fileName,'r')
#     str = f.read()
#     print(str)
# except FileNotFoundError:
#     print("file not found")
# finally:
#     if f is not None:
#         f.close()

# p4
# f = open("myfile.txt","w")
# while str != "@":
#     str = input('Enter the name'+'\n')
#     if str != '@':
#         f.write(str + '\n')
# f.close()

# p5
# f = open('myfile2.txt','a+')
# while str != "@":
#     str = input("Enter the names")
#     if str != '@':
#         f.write(str + "\n")
# f.seek(0,0)
# str2 = f.read()
# print(str2)
# f.close()

# p2 repetation

import os , sys
# fname = input('Enter the filename:')
# if os.path.isfile(fname):
#     f = open(fname,'r')
# else:
#     sys.exit()
# print('The file contents are: ')
# str = f.read()
# print(str)
# f.close()

# count -word,char,lines
fname = input('Enter the filename:')
if os.path.isfile(fname):
    f = open(fname,'r')
else:
    sys.exit()

cw = 0
cc = 0
cl = 0
for line in f:
    cl = cl + 1
    list = line.split()
    cw = cw + len(list)
    cc = cc + len(line)
print(cl)
print(cw)
print(cc)
f.close()



























