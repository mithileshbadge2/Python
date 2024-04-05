
# compile time error
# def add():
#     print(2+4)

# run time error

# print("hello")
# a = int(input("please enter the numberA"))
# b = int(input("Enter the numberB"))
# print(a/b)
# print("bye")

# print("hello")
# numbers = [11,22,5,6,8,1]
# print(numbers[6])
# print('bye')

# logical error

# def calculateBonusSalary(amount):
#     return amount * 0.10
# print(calculateBonusSalary(10000))


# print("hello")
# try:
#     e = int(input("enter the number A"))
#     f = int(input("enter the number B"))
#     print(e/f)
# except Exception:
#     print("please enter correct input")
# print("bye")

# try except else finally

# print("hello")
# names = ["monty","vedant","ram","vishal"]
# try:
#     m = int(input("enter the number A"))
#     n = int(input("enter the number B"))
#     print(m/n)
#     print(names[2])
# except ArithmeticError:
#     print('please enter the correct input')
# except IndexError:
#     print("add more element to list")
# except Exception:
#     print("Please correct the values")
# print("bye")



# print("hello")
# try:
#     m = int(input("enter the number A"))
#     n = int(input("enter the number B"))
#     print(m/n)
# except ArithmeticError:
#     print('please enter the correct input')
# finally:
#     print("I will always execute")
# print("bye")


print("hello")
try:
    m = int(input("enter the number A"))
    n = int(input("enter the number B"))
    print(m/n)
except ArithmeticError:
    print('please enter the correct input')
else:
    print("hello i will run")
finally:
    print("I will always execute")
print("bye")




















