class Father:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayName(self):
        print(self.firstName + self.lastName)

class Son(Father):
    def __init__(self, fn, ln,sn):
        super().__init__(fn, ln)
        self.sname = sn
    def displaySName(self):
        print(self.sname + self.lastName)
    
monty = Son('avinash','badge','monty')

print(monty.firstName)
print(monty.lastName)
monty.displayName()
monty.displaySName()


# multi -level
class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayGName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self, fn, ln,ffn):
        super().__init__(fn, ln)
        self.fname = ffn

    def displayFName(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self, fn, ln, ffn, ssn):
        super().__init__(fn, ln, ffn)
        self.sname = ssn
    def displaySName(self):
        print(self.sname + self.lastName)

MontyA = Son("mithilesh",'badge','avinash','monty')
print(MontyA.firstName)
print(MontyA.lastName)
print(MontyA.fname)
print(MontyA.sname)

MontyA.displayFName()
MontyA.displayGName()
MontyA.displaySName()

# herarical 
class Mother():
    
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayMName(self):
        print(self.firstName + self.lastName)
    
class Son(Mother):

    def __init__(self, fn, ln, ssn):
        super().__init__(fn, ln)
        self.sname = ssn
    def displaySName(self):
        print(self.sname + self.lastName)
    
class Daughter(Mother):

    def __init__(self, fn, ln,ddn):
        super().__init__(fn, ln)
        self.dname = ddn
    def displayDName(self):
        print(self.dname + self.lastName)

mithilesh = Son("preeti","badge","mithilesh")
Anushka = Daughter("preeti","badge","anushka")

print(mithilesh.firstName)
print(mithilesh.lastName)
print(mithilesh.sname)
mithilesh.displaySName()
mithilesh.displayMName()


print(Anushka.firstName)
print(Anushka.lastName)
print(Anushka.dname)
Anushka.displayMName()
Anushka.displayDName()

# multiple
class Mother:
    def __init__(self,fn,ln):
        print("mother constructor called")
        self.firstName = fn
        self.lastName = ln
    def displayName(self):
        print(self.firstName + self.lastName)

class Father:
    def __init__(self,fn,ln):
        print("Father Constructor called")
        self.firstName = fn
        self.lastName = ln
    def displayFName(self):
        print(self.fname + self.lastName)

class Son(Mother,Father):
    def __init__(self, fn, ln, ssn):
        super().__init__(fn, ln)
        self.sname = ssn
    def displaySName(self):
        print(self.sname + self.lastName)

monty = Son("mithilesh","badge","monty")


        
    
    






        

