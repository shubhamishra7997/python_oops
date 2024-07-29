# importing the modules 
from datetime import date
from typing import Any 
from dateutil.relativedelta import relativedelta 

class Product:
    def __init__(self, name):
        self.name = name
        print("Name of the product")

    def getExpData():
        raise NotImplementedError ("Subclasses should implement this method")
    

class Snack(Product):
    #variables (attributes) that are defined outside the constructor are constant for all 
    #object calls, i.e. they are class attributes. 

    shelf_life = 6  #This user need not give when object is created, class attribute and is 
                    #applicable to all objects of this class.

    #variables (attributes) that are defined inside the constructor are those that vary for all
    #object calls, i.e. they are instance attributes.

    def __init__(self, price, name):
        self.price = price #this user will give when object is created, instance attribute
        super().__init__(name)
        
    def print_details(self):
        #gets all the values from class attribute and instance attribute (constructors)
        print("name : " + self.name) 
        print("price : " + str(self.price)) 
        print("shelf life : " + str(self.shelf_life) + " months") 

    #take from user the pkdDate (which is inherited from the base class)
    def getExpData(self, pkdDate):
        expDate = pkdDate + relativedelta(months=self.shelf_life) 
        return expDate 

class Beverage(Product):
    shelf_life = 2 #years, class attribute

    def __init__(self, price, name): #constructor, with instance attributes
        self.price = price
        super().__init__(name)

    def  print_details(self):
        print("name is: ", self.name)
        print("Price is: ", self.price)
        print("Shelf life is: " + str(self.shelf_life) + " years.")

    def getExpData(self, pkddate):
        expdate = pkddate + relativedelta(years=self.shelf_life)
        return expdate

class Staples(Product):
    shelf_life = 5 #years, class_attribute

    def __init__(self, price, name):
        self.price = price #from user during object initialization, instance attribute
        super().__init__(name)

    def print_details(self):
        print("Name is: ", self.name)
        print("Price is: ", self.price)
        print("Shelf life is: " + str(self.shelf_life) + " years.")

    def getExpData(self, pkddate): #get pkd data from user, instance attribute for method
        expdata = pkddate + relativedelta(years=self.shelf_life)
        return expdata
    

def main():
    p = Product
    s = Snack(60,"cookies")
    s.print_details()
    s.shelf_life = 3 #i was able to modify the shelf life (although its a class variable) by using self.shel_life.
    print(s.name + " will expire on " + str(s.getExpData(date(2019, 10, 3))) + " months.")

    s1 = Snack(60,"cookies")
    s1.print_details()
    print(s.name + " will expire on " + str(s1.getExpData(date(2019, 10, 3))) + " months.")

    b = Beverage(200, "Cola")
    b.print_details()
    print(b.name + " will expire on " + str(b.getExpData(date(2019, 10, 3))) + " years.")

    st = Staples(5000, "Rice")
    st.print_details()
    print(st.name + " will expire on " + str(st.getExpData(date(2019, 10, 3))) + " years.")
    
if __name__ == '__main__':
    main()