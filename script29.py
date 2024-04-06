# A single try block can be follwed by several except block 
# Multiple except blocks can be used to handle multiple excpetions 
# We cannot write except block with try block
# We cannot write try block with except block
# Else block and finally block are not compulsory
# When there is no exception raised else block is executed after try block 
# Finally block is always executed

# p1
# try:
#     names = ["monty","vedant","nirnay"]
#     c = int(input("Enter the numberC"))
#     d = int(input("Enter the numberD"))
#     print(c/d)
#     print(names[2])
# except ArithmeticError:
#     print("please enter correct input")
# except IndexError:
#     print("please add the value")

# p2
# print("Hello")
# try:
#     print(34/0)
# finally:
#     print("I will always execute")
# print("bye")

# p3
# def calAvg(list):
#     [10,20,30][40]
#     total = 0
#     for item in list:
#         total = total + item
#     avg = total/len(list)
#     return total,avg
# try:
#     a,b = calAvg([1,2,3])
#     print(a)
#     print(b)
# except TypeError:
#     print("Enter the correct input")
# except ZeroDivisionError:
#     print("Arithmetic exception , enter correct value")
# except Exception:
#     print("please enter the correct input")


# print("hello")
# try:
#     x = 9
#     assert x > 1 and x <= 9
#     print(x)
# except AssertionError:
#     print("condition not matched")
# print("bye")

class lowBalance(Exception):
    def __init__(self,msg):
        self.msg = msg

def check(dict):
    for k,v in dict.items():
        if(v < 20000):
            raise lowBalance("Balance is low")
try:
    names = {"mithilesh":100000,"vedant":200000,"shobhit":500000,"rounak":80000}
    check(names)
    print(names)
except lowBalance as msg:
    print(msg)





