import unittest
from birdyboard import Birdyboard
# from unittest.mock import Mock, patch, DEFAULT - look into (de/serilize)

class TestBirdyboard (unittest.TestCase):

  @classmethod
  def setUp(self):
    self.birdyboard = Birdyboard()

  def test_user_created(self):
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




  #Test all options except quit and veriy a non valid entry fails
  def test_show_menu_option_choices(self):
    # self.assertEqual(self.birdyboard.show_menu(), '1')
    option = self.birdyboard.show_menu(1)
    self.assertEqual(1, option)

    # self.assertEqual([0, 1, 2, 3, 4], list(range(5)))

    # option = self.birdyboard.show_menu(2)
    # self.assertEqual(2, option)
    # option = self.birdyboard.show_menu(3)
    # self.assertEqual(3, option)
    # option = self.birdyboard.show_menu(4)
    # self.assertEqual(4, option)
    # option = self.birdyboard.show_menu(5)
    # self.assertEqual(5, option)
    # option = self.birdyboard.show_menu(6)
    # self.assertEqual(6, option)
    # option = self.birdyboard.show_menu(7)
    # self.assertEqual(False, option)
    # Decide if I need to test choices



if __name__ == '__main__':
    unittest.main()

# to run unittest...
# python birdyboard_tests.py -v

# to run coverage ...
# coverage run birdboard.py
# coverage report
# coverage report -a (to see all lines not covered)
# covrerage html (to create folder w report)
