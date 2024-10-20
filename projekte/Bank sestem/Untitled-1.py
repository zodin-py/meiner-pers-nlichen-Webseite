from abc import ABC, abstractmethod
import datetime

class Bank:
    def __init__(self, name, bank_swift_code):
      self.name = name
      self.swift_code = bank_swift_code
      self.customers = []

    def add_customer(self, customer):
       self.customers.append(customer)
        
class Customer:
  def __init__(self, name, address, phone_number, email):
   self.name = name
   self.address = address
   self.phone_number = phone_number
   self.email = email
   self.accounts = []

  def add_account(self, account):
    self.accounts.append(account)

class Account:
  def __init__(self, account_number):
    self.account_number = account_number
    self.balance = 0
    self.linked_card = None
    self.transacions_history = []

  def add_transacions(self, transaction):
    self.transaction_history.append(transaction)

class Card:
  def __init__(self, number, pin):
    self.number = number
    self.pin = pin
    
class Atm: 
 def __init__(self, bank, atm_location):
    self.bank = bank
    self.location = atm_location

class Transaction(ABC):
    transaction_counter = 0

    def __init__(self, transaction_type, amount=None):
      self.transaction_id = Transaction.transaction_counter
      self.timestamp = datetime.datetime.now()
      Transaction.transaction_counter += 1
      self.transaction_type = transaction_type
      self.amount = amount

    @abstractmethod
    def execute(self):
       pass

class WithdrawTransaction(Transaction):
    def __init__(self, amount):
        super().__init__("withdrawal", amount)
        self.amount = amount

    def execute(self, account):
        if account.balance >= self.amount:
            account.balance -= self.amount
            print(f"Withdrawal Successful. New Balance: {account.balance}")
            account.add_transactions(self)
        else:
            print("Insufficient balance")

class DepositTransaction(Transaction):
    def __init__(self, amount):
        super().__init__("deposit", amount)
        self.amount = amount
        
    def execute(self, account):
        account.balance += self.amount
        print(f"Deposit Successful. New Balance: {account.balance}")
        account.add_transactions(self)

class BalanceInpuiry(Transaction):
    def __init__(self):
      super().__init__("balance inpuiry")
      

    def execute(self, account):
       print("Your balaince is: {account.balance}")
       account.add_transiction(self)
       
       for transaction in self.transaction_hestory.items():
          print(f"Transaction : {transaction} in {self.timestamp}")
                

my_bank = Bank("ZDAN", "HSBCEGXX")
customer_1 = Customer("mhdi", "Fortunastraße 6" ,"01634251236" , "mohamed@gmil.com")
account_1 = Account("4659")

customer_1.add_account(account_1)
my_bank.add_customer(customer_1)


informations = my_bank.customers[0].phone_number, my_bank.customers[0].name

for information in informations:
  print(informations[0])
