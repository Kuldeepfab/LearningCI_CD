import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):


    """
    self.emp_1 = Employee('Corey','Schafer',50000)
    self.emp_2 = Employee('Sue','Smith',60000)
    The Above Two lines we are written in the beinging of each TestFunction.
    Therfore for doing this in a better way ,Use setUp and tearDown
    shown belows
    after applying using Tear and setup , we need to replace all <emp_1> 
    by <self.emp_1> 
    """

    """
    print statement in each testcase, showing how this Setup function
    is called in the begining of any testfunction and ends up with teardown
    """

    """
    Now we have used Classmethod , while writing setUp and tearDown,
    the reason behind this, earlier we are working on instance(i.e self), now 
    we are working on class (i.e cls)
    """

    @classmethod
    def setUpClass(cls):
        print('setupClass')
    
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')


    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey','Schafer',50000)
        self.emp_2 = Employee('Sue','Smith',60000)

    def tearDown(self):
        print('teardown\n')

    def test_email(self):
        print('test_email')
        #emp_1 = Employee('Corey','Schafer',50000)
        #emp_2 = Employee('Sue','Smith',60000)
        
        self.assertEqual(self.emp_1.email,'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email,'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        #emp_1 = Employee('Corey','Schafer',50000)
        #emp_2 = Employee('Sue','Smith',60000)

        self.assertEqual(self.emp_1.fullname,'Corey Schafer')
        self.assertEqual(self.emp_2.fullname,'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        #emp_1 = Employee('Corey','Schafer',50000)
        #emp_2 = Employee('Sue','Smith',60000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay , 52500)
        self.assertEqual(self.emp_2.pay , 63000)



if __name__ == '__main__':
    unittest.main()