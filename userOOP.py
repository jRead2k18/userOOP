class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit (self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.name, "- Balance:", self.account_balance)
    def transfer_money(self, account, amount):
        self.account_balance -= amount
        account.account_balance += amount
        print(self.name, "- Balance:", self.account_balance)
        print(account.name, "- Balance:", account.account_balance)


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
bonzi = User("BonziBuddy", "BonziBuddy@buddy.com")

guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(200)
guido.make_withdrawal(50)

guido.display_user_balance()

monty.make_deposit(150)
monty.make_deposit(345)
monty.make_withdrawal(170)
monty.make_withdrawal(65)

monty.display_user_balance()

bonzi.make_deposit(500000)
bonzi.make_withdrawal(5)
bonzi.make_withdrawal(3)
bonzi.make_withdrawal(462841)

bonzi.display_user_balance()

guido.transfer_money(bonzi, 100)