class Person:
    fn = "mahesh"
    ln = "patil"

    def display(self):
        print(self.fn + self.ln)

mahesh = Person()
mahesh.display()
suresh = Person()
suresh.display()

suresh.fn = 'suresh'
suresh.ln = 'patil'
suresh.display()

class Person:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    
    def display(self):
        print(self.firstName + self.lastName)

mithilesh = Person("mithilesh","badge")
print(mithilesh.firstName)
print(mithilesh.lastName)
mithilesh.display()

vedant = Person("vedant","gaikwad")
vedant.display()