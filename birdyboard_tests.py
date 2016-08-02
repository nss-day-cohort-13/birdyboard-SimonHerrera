import unittest
from birdyboard.py import Birdyboard
# from unittest.mock import Mock, patch, DEFAULT - look into (de/serilize)

class TestBirdyboard (unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.birdyboard = Birdyboard()

  def test_user_created(self):
    # tests to go here


  def test_user_selected(self):
    # tests to go here


  def test_view_chirps(self):
    # tests to go here


  def test_write_public_chirp(self):
    # tests to go here


  def test_write_private_chirp(self):
    # tests to go here




  #Test all options except quit and veriy a non valid entry fails
  def test_menu_option_choices(self):
    # Decide if I need to test choices



if __name__ == '__main__':
    unittest.main()
    # print('Running')
