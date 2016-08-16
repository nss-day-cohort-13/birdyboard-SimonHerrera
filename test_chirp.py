import unittest
from chirp import *
from user import *


class TestChirp(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

# ******************* NEW USER ****************************
  def test_new_chirp_creation(self):
    user = User("Blake Rivers", 'brivers')
    chirp = Chirp(
              user_uuid = user.user_uuid,
              chirp_message = "Hey, How are you doing?"
              )
    # will create chirp_uuid
    # will create private = False
    # will create receiver = None
    self.assertEqual(chirp.chirp_message, "Hey, How are you doing?")
    self.assertEqual(chirp.user_uuid, chirp.user_uuid)
    self.assertEqual(chirp.private, False)
    self.assertEqual(chirp.receiver, None)
    self.assertIsInstance(chirp, Chirp)
    self.assertIsNotNone(chirp.chirp_uuid)

if __name__ == '__main__':
  unittest.main()

# python -m unittest discover -p "test_*"