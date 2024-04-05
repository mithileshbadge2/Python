class Bank:

    country = "India"
    count = 0

    def __init__(self,fn,ln,acc,bal):
        self.firstName = fn
        self.lastName = ln
        self.accNo = acc
        self.balance = bal
        self.transactions = []
        Bank.count = Bank.count + 1
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transactions.append(amount)
    
    def withdrawl(self,amount):
        if(self.balance > amount):
            self.balance = self.balance - amount
            self.transactions.append(-amount)
        else:
            print("Insufficient balance")

    def lastFiveTransaction(self,x):
        return self.transactions[-x::]
    
    @classmethod
    def changeCountry(cls,cl):
        cls.country = cl

    @staticmethod
    def objCount():
        return Bank.count
    
mithilesh = Bank("mithilesh",'badge',123,1000)
vedant    = Bank("vedant",'gaikwad',456,2000)
shobhit   = Bank("shobhit",'harde',789,3000)
shishir   = Bank("shishir",'jain',987,4000)
rounak    = Bank("rounak",'gupta',654,5000)

print(Bank.objCount())
mithilesh.withdrawl(10000000)
mithilesh.deposit(3000000)
mithilesh.deposit(30000)
print(mithilesh.lastFiveTransaction(1))

    




    

