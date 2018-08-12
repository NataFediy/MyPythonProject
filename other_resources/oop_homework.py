# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples
# and return the slope and distance of the line.

class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


# EXAMPLE OUTPUT

coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())
print('-' * 21)


# Problem 2
# Fill in the class
class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * (self.radius) ** 2

    def surface_area(self):
        top = 3.14 * (self.radius) ** 2
        return (2 * top) + (2 * 3.14 * self.radius * self.height)


# EXAMPLE OUTPUT
c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
print('-' * 21)


# Object Oriented Programming Challenge
# For this challenge, create a bank account class that has two attributes:
#
# owner
# balance
# and two methods:
#
# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals,
# and test to make sure the account can't be overdrawn.
class Account:
    role = 'customer'

    @staticmethod
    def sum(a, b):
        return a + b

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, money):
        self.balance += money
        print(f'Deposit Accepted\nAdded {money} to the balance'
              f'\nThe current balance is {self.balance}')

    def withdraw(self, wd_ammount):
        if self.balance >= wd_ammount:
            self.balance -= wd_ammount
            print('Withdrawal Accepted\nThe new balance is {}'.format(self.balance))
        else:
            print('Funds Unavailable!')


balance = 0
acct2 = Account('Nata', 50)
acct1 = Account('Jose', 100)

print('Account owner: {}'.format(acct1.owner))
print('Account ballance: {}'.format(acct1.balance))

print(acct1.owner)
print(acct1.balance)
print('Who is {}? - {}'.format(acct1.owner, Account.role))

acct1.deposit(250)
acct1.withdraw(75)
acct1.withdraw(750)

print(acct2.sum(50, 20))
