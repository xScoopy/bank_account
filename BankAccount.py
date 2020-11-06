class BankAccount:
    """Defining class attributes for class BankAccount"""

    routing_number = "123456070"

    def __init__(self, full_name, account_number, balance):
        """Defining instance attributes for class BankAccount"""
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
