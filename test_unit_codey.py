class Employee:

    amount_raise = 1.05
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.amount_raise)

emp_1 = Employee('Shubham', 'Mishra', 65000)
emp_2 = Employee('Shivam', 'Mishra', 62500)








