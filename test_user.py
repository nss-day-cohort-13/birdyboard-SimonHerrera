import unittest
from user import *


class TestUser(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

# ******************* NEW USER ****************************
  def test_new_user_creation(self):
    user = User(
              full_name = "David Williams",
              user_name = "dwilliams"
              )


    self.assertEqual(user.full_name, "David Williams")
    self.assertEqual(user.user_name, "dwilliams")
    self.assertIsInstance(user, User)
    self.assertIsNotNone(user.user_uuid)

if __name__ == '__main__':
  unittest.main()

# python -m unittest discover -p "test_*"