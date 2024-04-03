# class Person:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
    
#     def display_name(self):
#         print(self.firstName + self.lastName)

# mithilesh = Person("mithilesh","badge")
# vedant = Person("vedant","gaikwad")
# print(mithilesh.firstName)
# print(vedant.firstName)
# print(mithilesh.lastName)
# print(vedant.lastName)
# mithilesh.display_name()
# vedant.display_name()

class Person2:
    country = "Bharat"
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def display_name(self):
        print(self.firstName + self.lastName)
    
    @classmethod
    def changeCountry(cls,cnty):
        cls.country = cnty

nirnay = Person2("nirnay","bhau")
monty = Person2("monty","badge")
shaam = Person2('shaam','dev')

print(nirnay.firstName)
print(nirnay.lastName)
print(nirnay.country)
nirnay.country = "India"
print(nirnay.country)
print(monty.country)
print(shaam.country)
Person2.changeCountry("Hindustan")
print(nirnay.country)
print(monty.country)
print(shaam.country)

