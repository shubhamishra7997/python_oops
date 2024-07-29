#video 5
#Special methods: Magic/Dunder


class Employee:

    #class attribute
    raise_amount = 1.04

    #instance attribute in Class
    def __init__(self, first, last, pay): #constructor, self is the instance (emp_1 or emp_2 here)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
    def fullname(self): #do not forget the self in method
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
 
    #repr is meant to be an umabigious representation of the object.
    #used for debuging and logging.
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    #readable representation of an object for the user.
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other): #sum of 2 employees salaries.
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee("Shubham", "Mishra", 65000) 
emp_2 = Employee("Shivam", "Mishra", 62500)

#5.1
print(emp_1) #gives a vague output.

#5.2
#dunder repr and str
#try to atlease have an repr method, coz it is fallback for str.
print(repr(emp_1)) #or print(emp_1.__repr__())
print(emp_2.__str__())

#5.3
#dunder add
print(emp_1 + emp_2)
#0r 
print(emp_2.__add__(emp_1))

#5.4 dunder len (total number of characters in an employee name)
print(len(emp_1))
print(emp_2.__len__())



