from random import randint
#Imported random for account number generation

account_numbers = []
#List for holding account numbers to see if they already exist. (Would normally be stored in a database or something)

def create_acct():
    """create a random account number, 
    and check to ensure it doesnt already exist"""
    random_account = randint(10000000, 99999999)
    while random_account in account_numbers:
        random_account = randint(10000000, 99999999)
    return random_account

def hide_acct(acct_num):
    """function to hide the first four digits of the account number"""
    new_acct = list(str(acct_num))
    for num in range(5):
        new_acct.insert(0,'*')
        del new_acct[num]
    hidden_acct = ""
    return hidden_acct.join(new_acct)

class BankAccount:
    """Defining class attributes for class 
    BankAccount; Routing number is hard coded """

    routing_number = "123456070"

    def __init__(self, full_name):
        """Defining instance attributes for class BankAccount 
        with random 8 digit acct number and balance of 0"""
        self._full_name = full_name
        self._account_number = create_acct()
        self._balance = 0
        account_numbers.append(self._account_number)

    def deposit(self, amount):
        """Method to deposit an amount, add it to the balance, 
        and print the amount deposited"""
        self._balance += amount
        print(f'Amount deposited: ${amount}')
        return

    def withdraw(self, amount):
        """Method to withdraw an amount, subtracting it 
        from the balance and printing a message for the amount withdrawn. 
        If the user 'overdrafts', they will be informed of insufficient funds and charged an overdraft fee."""
        if amount > self._balance:
            print("Insufficient Funds")
            self._balance -= 10
            return
        else:
            self._balance -= amount
            print(f'Amount withdrawn: ${amount}')
            return

    def get_balance(self):
        """Method to get the balance. Prints a friendly statement and returns the balance"""
        print(f'Hello {self._full_name}, your balance is: ${"{:.2f}".format(self._balance)}')
        return self._balance
    
    def add_interest(self):
        """Method to add monthly interest at a rate of 1% per year"""
        self._balance += self._balance * 0.00083
        return
    
    def print_receipt(self):
        """Method to print a receipt containing name, acct and routing numbers, then balance."""
        print(self._full_name)
        print(f'Account No.: {hide_acct(self._account_number)}')
        print(f'Routing No.: {self.routing_number}')
        print(f'Balance: ${"{:.2f}".format(self._balance)}') #formatting balance to 2 decimal places to avoid the extensively long decimal places
        return

#Creating 3 examples of BankAccount objects 
scoop_account = BankAccount("Scoopy Scoopertins")
joi_account = BankAccount("Joi Anderson")
jess_account = BankAccount("Jess Dahmen")

#There are several print statements to assist with readability in the terminal for showcasing the examples. 
#printing account numbers to show they are not hard coded
print(scoop_account._account_number)
print(joi_account._account_number)
print(jess_account._account_number)
print(' ')
#Depositing different amounts on each of the 3 accountss
scoop_account.deposit(1500.42)
joi_account.deposit(2500.78)
jess_account.deposit(5000.00)
print(' ') 

#Withdrawing money examples, followed by printing the balance to show that the overdraft for scoop charged a 10 dollar fee. 
scoop_account.withdraw(1600)
scoop_account.get_balance()
print(' ')
joi_account.withdraw(1000)
joi_account.get_balance()
print(' ')
jess_account.withdraw(5.67) #for a double double at in n out burger
jess_account.get_balance()
print(' ')

#adding interest and printing the balance out to show it working
scoop_account.add_interest()
scoop_account.get_balance()
print(' ')
joi_account.add_interest()
joi_account.get_balance()
print(' ')
jess_account.add_interest()
jess_account.get_balance()
print(' ')

#printing receipt examples
scoop_account.print_receipt()
print(' ')
joi_account.print_receipt()
print(' ')
jess_account.print_receipt()



