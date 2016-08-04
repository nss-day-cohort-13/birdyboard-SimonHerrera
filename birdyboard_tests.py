import unittest
from birdyboard import Birdyboard
# from unittest.mock import Mock, patch, DEFAULT - look into (de/serilize)

class TestBirdyboard (unittest.TestCase):

  @classmethod
  def setUp(self):
    self.birdyboard = Birdyboard()

  def test_user_created(self):
    # self.user = Birdyboard()
    self.user = self.birdyboard.create_user("Dennis Johnson", "dtrain")
    self.assertEqual("dtrain", self.user)

    assert 1 == 1
    # actual tests to go here


  def test_user_selected(self):
    assert 2 == 2
    # actual tests to go here


  def test_view_chirps(self):
    assert 3 == 3
    # actual tests to go here


  def test_write_public_chirp(self):
    assert 4 == 4
    # actual tests to go here


  def test_write_private_chirp(self):
    assert 5 == 5
    # actual tests to go here



if __name__ == '__main__':
    unittest.main()

# to run unittest...
# python birdyboard_tests.py -v

# to run coverage ...
# coverage run birdboard.py
# coverage report
# coverage report -a (to see all lines not covered)
# covrerage html (to create folder w report)
