#can you create a vehicle class using OOP.
# include in your initializer the color of the car, how old the car is and how many seats this car has.

class Vehicle:
    def __init__(self, color, year, seat):
        self.color = color
        self.year = year
        self.seat = seat

    def age_of_car(self):
        age = 2024 - self.year
        print("The car is ", age, " years old" )
    
    def print_color(self):
        print("Color of the car is: " + self.color)

    def print_seats(self):
        print("Seats in the car is: ", self.seat)

def main():
    v = Vehicle("Blue", 2010, 2)
    v.age_of_car()
    v.print_color()
    v.print_seats()

if __name__ == '__main__':
    main()


