class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Customer[{self.id}, {self.firstname}, {self.lastname}]'


class AccountTransaction:
    last_id = 0

    def __init__(self, account, amount, transaction_type):
        AccountTransaction.last_id += 1
        self.id = AccountTransaction.last_id
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    def __repr__(self):
        return f'AccountTransaction[{self.id}, {self.account.id}, {self.amount}, {self.transaction_type}]'


class Account:
    last_id = 1000

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0
        self.transactions = []

    def deposit(self, amount):
        # TODO: Implement validation
        if type(amount) != int or amount < 0:
            raise InvalidAmountException(f'Amount is invalid {amount}')
        self._balance += amount
        transaction = AccountTransaction(self, amount, 'Deposit')
        self.transactions.append(transaction)

    def charge(self, amount):
        # TODO: Implement validation
        if type(amount) != int or amount < 0:
            raise InvalidAmountException(f'Amount is invalid {amount}')
        if amount > self._balance:
            raise InsufficientFundsException(f'Insufficient funds in account {self.id}')
        self._balance -= amount
        transaction = AccountTransaction(self, amount, 'Charge')
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

    def __repr__(self):
        return f'Account[{self.id}, {self.customer.lastname}, {self._balance}]'


class Bank:
    def __init__(self):
        self.customer_list = []
        self.account_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def transfer(self, from_account_id, to_account_id, amount):
        # TODO: Implement validation
        from_account = self.find_account(from_account_id)
        to_account = self.find_account(to_account_id)

        if not from_account or not to_account:
            raise BankException("Invalid account IDs provided for transfer")

        from_account.charge(amount)
        to_account.deposit(amount)

    def find_account(self, account_id):
        for account in self.account_list:
            if account.id == account_id:
                return account
        return None

    def __repr__(self):
        return f'Bank[{self.customer_list}; {self.account_list}]'


class BankException(Exception):
    pass

class InsufficientFundsException(BankException):
    pass

class InvalidAmountException(BankException):
    pass

bank = Bank()

c = bank.create_customer('Alice', 'Johnson')  # Changed from 'John' and 'Brown'
print(c)
a = bank.create_account(c)
a2 = bank.create_account(c)
print(a)

c2 = bank.create_customer('Eva', 'Miller')  # Changed from 'Anne' and 'Smith'
a3 = bank.create_account(c2)
print(bank)
print('--------')

try:
    a.deposit(330)
    a3.deposit(-100)
    a2.deposit(-50)
except BankException as ie:
    print(f'Something went wrong {ie}')
else:
    print('Run it when no exception occurred')

print('before transfer')
print(bank)

try:
    bank.transfer(1003, 1002, 140)
except BankException as ie:
    print(f'Something went wrong {ie}')
else:
    print('Transfer successful')

print('after transfer')
print(bank)

print("Transaction history for account a3:")
for transaction in a3.get_transactions():
    print(transaction)