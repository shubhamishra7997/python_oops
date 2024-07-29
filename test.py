import unittest

class Bankaccount:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
    
    def deposit(self, amount):
        self.balance += amount
        return True
    
# we create a subclass Testbankoperations of unittest.Testcase.
# we assert False to get an expected outcome of test failure.

class Testbankoperations(unittest.TestCase):
    def test_insufficient_balance(self):
        #Arrange (setup/precondition)
        # during the arrange phase, all objects and variables need to be set.
        a = Bankaccount(1)
        a.deposit(100)
        #Act
        # During the act phase, the function/method/class under test is called.
        outcome = a.withdraw(200)
        #Assert
        # We verify the outcome of the test.
        self.assertFalse(outcome)

    def test_negative_amount(self):
        #Arrange
        a = Bankaccount(2)
        #Act
        outcome = a.deposit(-200)
        #assert
        self.assertFalse(outcome)

