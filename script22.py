# class Person:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#     def displayName(self):
#         print(self.firstName + self.lastName)
#     def updateName(self,fn):
#         self.firstName = fn

# monty = Person("monty","badge")
# print(monty.firstName)
# print(monty.lastName)
# monty.displayName()
# monty.updateName("mith")

# print(monty.firstName)       


















class Person2:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayName(self):
        print(self.firstName + self.lastName)
    def updateName(self,fn):
        self.firstName = fn


monty = Person2("monty","badge")
print(monty.firstName)
print(monty.lastName)
monty.displayName()
monty.updateName("mithilesh")
print(monty.firstName)