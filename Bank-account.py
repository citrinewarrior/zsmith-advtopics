#Make a class BankAccount where instances of accounts can be created.
#Give these objects variables such as account number, account owner, and account balance.
#Create methods to deposit, withdraw, and check balance.
class BankAccount:
#SET BALANCE IN THE INIT TO 0
    def __init__(self,number,owner):
        self.number = number
        self.owner = owner
        self.balance = 0


    def displayaccolder(self):
        print "Account Number:", self.number
        print "Account Holder:", self.owner
        print "Current Balance:", self.balance

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        self.balance = self.balance - amount

    def checkbalance(self):
        print "Your current account balance is: ", self.balance, "dollars"

#down here, are existing test accounts.
acc1 = BankAccount(1337, "Noodle")
acc2 = BankAccount(2005, "2D")
acc3 = BankAccount(666, "Murdoc")
acc4 = BankAccount(32, "Russel",)


acc1.deposit(50)
acc1.displayaccolder()
acc1.withdraw(25)
acc1.checkbalance()






#down here goes the code to display the information
