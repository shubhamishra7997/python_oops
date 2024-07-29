class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + '.' +last + '@company.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    #6.1 property decorator
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    
    #6.2 
    @fullname.setter
    def fullname(self, name): #name is what we are going to set.
        first, last = name.split(' ')
        self.first = first
        self.last = last

    #6.3
    @fullname.deleter
    def fullname(self): #name is what we are going to set.
        print('Delete Name!')
        self.first = None
        self.last = None
   
emp_1 = Employee('Shubham', 'Mishra', 65000)
emp_2 = Employee('Shivam', 'Mishra', 62500)

#video 6

#getter, setter and deleter attributes.

emp_1.first='Jim'
print(emp_1.first)
print(emp_1.email)
#print(emp_1.fullname()) 

#Problem:  This just not change the email.
#Reason is that during the object initialization there is email being assigned which gets the old value.

#6.1 
#how to fix this, so that email gets automatically updated.
# solution: using property decorator.
# These allow to define a method and access it like an attribute

emp_1.first='Jim'
print(emp_1.first)
print(emp_1.email)  #email is now defined as a method but accessed like an attribute
print(emp_1.fullname) #fullname is now defined as a method but accessed like an attribute

#6.2 setter
print("----------------6.2 setter---------------------")
emp_1.fullname = 'Akshay Kumar' #error: cant set the attribute
print(emp_1.first)
print(emp_1.email) 
print(emp_1.fullname) 

#6.3 deleter
print("----------------6.3 deleter---------------------")
del emp_1.fullname 






