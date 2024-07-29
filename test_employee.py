import unittest
from test_unit_codey import Employee

#keep your code DRY: Dont Repeat Yourself
class TestEmployee(unittest.TestCase):

    #At the beginning of the test (only once)
    @classmethod
    def setUpClass(cls):
        print('SetUpClass')

    #At the end of the test (only once)
    @classmethod
    def tearDownClass(cls):
        print('TearDownclass')

    #Runs before every single test
    def setUp(self):
        print('SetUp')
        self.emp_1 = Employee('Akshay', 'Kumar', 50000)
        self.emp_2 = Employee('Ajay', 'Devgan', 60000)

    # Runs after every single test
    def tearDown(self):
        print('Teardown')
        pass

    #create employees, check emails, change first name, recheck email.
    def test_email(self):
        print('Test Email')
        self.assertEqual(self.emp_1.email, 'Akshay.Kumar@company.com')
        self.assertEqual(self.emp_2.email, 'Ajay.Devgan@company.com')

        self.emp_1.first = 'Dimple'
        self.emp_2.first = 'Kajol'

        self.assertEqual(self.emp_1.email, 'Dimple.Kumar@company.com')
        self.assertEqual(self.emp_2.email, 'Kajol.Devgan@company.com')

    def test_fullname(self):
        print('Test Fullname')
        self.assertEqual(self.emp_1.fullname, 'Akshay Kumar')
        self.assertEqual(self.emp_2.fullname, 'Ajay Devgan')

if __name__ == '__main__':
    unittest.main()
