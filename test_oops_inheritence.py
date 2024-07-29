import pytest
from oops_inheritance import Staples, Beverage, Snack
from datetime import date

# define test class
# define multiple sub tests, check for name, expiry date, price and shelf life.
# repeat for all 3

class TestSnack:

    #first test to check the name, price and shelf life
    def test_one(self):
        s = Snack(60, "cookies")
        assert ("cookies", 60, 6) == (s.name, s.price, s.shelf_life)

    #second test to check the expiry date
    def test_two(self):
        s = Snack(100, "chips")
        expiry = s.getExpData(date(2019, 10, 3))
        assert expiry == date(2020, 4, 3)

class TestStaple:
    def test_staple_one(self):
        #arrange with act
        st = Staples(200, "wheat") #shelf life is fixed for 2 years
        #assert
        assert (200, "wheat", 2) == (st.price, st.name, st.shelf_life)

    def test_staple_two(self):
        #arrange
        st2 = Staples(500, "corn")
        #act
        expirydate = st2.getExpData(date(2020, 10, 3))
        #assert
        assert expirydate == date(2022, 10 ,3)

