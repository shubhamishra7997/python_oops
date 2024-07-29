# Video 1 
# creating and instantiating classes
# data = attributes
# function = methods

class Employee:

    #class attribute
    num_of_emps = 0
    raise_amount = 1.04

    #instance attribute in Class
    def __init__(self, first, last, pay): #constructor, self is the instance (emp_1 or emp_2 here)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1 #not using self, becuase I do not want the instance to overwrite this.

    def fullname(self): #do not forget the self in method
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #3.1 class method
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    #3.2 alternative constructor
    @classmethod
    #naming convention that alt const starts with from_
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-") #split data for creating objects in below line.
        return cls(first, last, pay) #same as Employee(first, last, pay) to create new objects.
    
    #3.3 static method
    @staticmethod
    #giveaway that a method is static method is that there is no metion of self, cls or any instance variables or class variables.
    def is_workday(day): #no need of any cls or self.
        if day.weekday() == 5 or day.weekday() == 6: #inbuilt python function for weekdays where Monday = 0, Sunday = 6.
            return False
        return True
    
emp_1 = Employee("Shubham", "Mishra", 65000) 
emp_2 = Employee("Shivam", "Mishra", 62500)
#-----------------------------------------------------------------------------------------#
#video 4
# Inheritence - Allows to inherit attributes and methods from parent class.
# we can create sub classes, and get functionalites of parent class, use them or overwrite them and create new functionalites.
# without affecting the parent class in any way.

# 4.1 
# create developers and managers sub-classes with name, email and pay.

#4.1 create subclass
class Developer(Employee):

    #4.2 simple change
    raise_amount = 1.10

    #4.3 complex change
    def __init__ (self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #super will take the inputs from developers and pass it to employees init method.
        #other way
        #Employee.__init__(self, first, last, pay) #this is not helpful for multiple inheritance.
        self.prog_lang = prog_lang

# dev_1 = Developer("Akshay", "Kumar", 95000)
# dev_2 = Developer("Ajay", "Devgan", 100000)

# Python first tries to look at the Developer class to find any attributes for first, last and pay. 
# Since it does not see any, it goes up the chain of interitance to get the fist, last and pay into the parent class.
# This is known as method resolution order.

# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)

#4.2 make a change in class attribute
#give developers a 10% raise
# so here we add a class attribute in the subclass. 
# print(dev_1.pay) 
# print(dev_1.raise_amount) 
# dev_1.apply_raise()
# print(dev_1.pay)

#4.3 make complex change
# give your developer a programming language as an attribute.
# currently, constructor of employee does not have that, so we need to give the developer class its own init method (constructor).
dev_1 = Developer("Akshay", "Kumar", 95000, "Python")
dev_2 = Developer("Ajay", "Devgan", 100000, "Java")

# we got all employee code for free and had added a simple prog lang.
# print(dev_1.email)
# print(dev_1.prog_lang)
# print(dev_2.email)
# print(dev_2.prog_lang)

#4.4 Manager subclass
#manages employees, can add employee, remove employee, print all employees.
class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else: 
            self.employees = employees

    def add_emps(self, emps):
        self.employees.append(emps)

    def remove_emps(self, emps):
        self.employees.remove(emps)

    def print_all_emps(self):
        for emp in self.employees:
            print("Manages -->", emp.fullname())

#4.4.1
#create manager subclass
mgr_1 = Manager("Rohit", "Shetty", 78000, [dev_1])

#4.4.2
#check if successfull created
# print(mgr_1.email)
# print(mgr_1.print_all_emps())

#4.4.3
#add employee
# mgr_1.add_emps(dev_2)
# print(mgr_1.print_all_emps())

#4.4.4
#remove employee
# mgr_1.remove_emps(dev_1)
# print(mgr_1.print_all_emps())

#4.5 isinstance: It will tell if an object is an instance of a class.
# print(isinstance(mgr_1, Manager)) #true
# print(isinstance(mgr_1, Employee)) #true
# print(isinstance(mgr_1, Developer)) #false

#4.6 issubclass: It will tell if a class is a sublass of another
# print(issubclass(Manager, Employee)) #true
# print(issubclass(Developer, Employee)) #true
# print(issubclass(Manager, Developer)) #false

#-----------------------------------------------------------------------------------------#
#print(Employee.num_of_emps)

#emp_1 = Employee("Shubham", "Mishra", 65000) #instance is passed automatically, so no need to write self = emp_1
# on the above line, it will do the follwing: 
# emp_1.first = "Shubham"
# emp_1.last = "Shubham"
# emp_1.pay = 65000
# emp_1.email = "Shubham.Mishra@company.com"
#emp_2 = Employee("Shivam", "Mishra", 62500)

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname()) #need brackets here becuase this is a method (function).
# print(emp_2.fullname())

#The above lines are converted as below:
# Employee.fullname(emp_1) #need to pass the instance that is equal to self.
# Employee.fullname(emp_2)

#What I learned here: how to create class, how to create instance of a class (object),
# initialize class attributes (constructor) and create methods

#-----------------------------------------------------------------------------------------#
#video 2
# class variables (attributes): Common variables shared amongst all class instances.

#2.1 class variable with self in methods
#lets say that the company bonus is common for all employees.

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.raise_amount) #class attribute raise_amount is directly accessed by the class
# print(emp_1.raise_amount) # if we try to call an atribute on an instance, it will first check if the instance attribute contains that attribute.
# # if it doesnt, then it checks if any class or any super class has that attribute.
# print(emp_2.raise_amount)

# print(emp_1.__dict__)
# print(Employee.__dict__)

# Employee.raise_amount = 1.05
# Here the employee raise amount leads to the class attribute to be changed, meaning that all the instances get an updated value.
# print(Employee.raise_amount) 
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# emp_1.raise_amount = 1.05
# #Here only emp_1 raise amount changes, and class attribute raise amount remains to 1.04, emp_2's raise amount remains to 1.04
# # This is becuase now, this raise_amount becomes a instance attirbute for emp_1.
# # This happens only because in the class we had: self.raise_amount (which allows instance to overwrite the value of class variable)
# print(Employee.raise_amount) 
# print(emp_1.raise_amount)
# print(emp_1.__dict__)
# print(emp_2.raise_amount)
# print(emp_2.__dict__)

#2.2 class variable without self
#track the number of employees num_of_emps
# print(Employee.num_of_emps)
#if you use the same above fucntion before creating objects, then it will be 0.

#-----------------------------------------------------------------------------------------#
#video 3
# regular methods, class methods and static methods.

#3.1 class method
#regular methods take instance as first argument, eg;  emp_1. 
#but what if we want to send "Employee" the class as an argument ? 
# for this we use class methods.
#in order to have a class methods, you need to add a @classmethod decorator on top of the method. 
# then pass the argument "cls" instead of "self" to the method.

# #all are set to 4 percent
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# #now to change the value of raise amount without touching the class Employee code, we can use the class method.
# Employee.set_raise_amount(1.05) #no need to mention cls = Employee, it is done automatically.
# # This is same as Employee.raise_amount = 1.05, but by using class method.

# #all are set to 5 percent
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#3.2 Alternative constructors
#you can use class methods in order to provide multiple ways of creating objects.

#lets say, someone has a string of data about user information, and wants to make use of employee class.
# instead of parsing the strings again and again, is there any other way?

# emp_str_1 = "John-Doe-70000"
# emp_str_2 = "John-Smith-80000"
# emp_str_3 = "John-Stevens-90000"

# #parsing strings with alternative constructor
# emp_3 = Employee.from_string(emp_str_1)
# emp_4 = Employee.from_string(emp_str_2)
# emp_5 = Employee.from_string(emp_str_3)

# print(emp_3.email)
# print(emp_4.pay)
# print(emp_5.last)

#3.3 Static methods
# Regular methods take instance (self) as the first argument.
# Class methods take class (cls) as the first argument.
# STATIC METHODS DONT TAKE ANY ARGUMENT AUTOMATICALLY. They are like regular functions inside a class.

#example: we want a simple function that takes a date and tells if it was a working date on not. 
# This has a logical connection to the class, hence we define it inside the class, but it does not depend on any instance variable or class variable.

# import datetime
# my_date = datetime.date(2024, 7, 28) #sunday
# my_date_2 = datetime.date(2024, 7, 29) #monday

# print(Employee.is_workday(my_date))
# print(Employee.is_workday(my_date_2))


