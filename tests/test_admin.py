
import unittest
from app.models import Admin
class UserModelTest(unittest.TestCase):
    '''
    Test class to test behaviours of the [Class] class
    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = Admin(password_hash = 'jose')
    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('jose'))