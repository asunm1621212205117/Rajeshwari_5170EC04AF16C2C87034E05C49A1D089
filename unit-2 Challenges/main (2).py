class BankAccount:

def _innit_(self,account_number,account_holder_name,initial_balance=0.0):
  self._account_number=account_number
  self._account_holder_name=account_holder_name
  self._Account_balance=initial_balance

def deposit(self,amount):
  if amount>0:
    self._account_balance+=amount
    print("Deposited ${}.New balance:${}".format(amount,self._account_balance))

else:
print("Invalid deposit amount.please deposit a positive amount.")

def withdraw(self,amount):
  if amount>0 and amount <= self._accoun_balance:
    self._account_balance-=amountprint("Withdraw ${}.New balance:${}".format(amount,self._account_balance))

else:
print("Invalid withdrawal amount or insufficient balance.")

def display_balance(self):
  print("Account balance for{}(account#{}):${}".format(self._account_holder_name,self._account_number,self._account_balance))

account=bankAccount(account_number="123456789".account_holder_name="pooja",
              initial_balance=10000.0)
account.display()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()

