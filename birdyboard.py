import sys
import pickle

class Birdyboard:

  def __init__(self):
    pass

  def show_menu(self):
    while True:
      # Main loop, for use in getting function we want to run, must be 1-6
      print("""#########################################
##           Birdyboard~~~~~           ##
#########################################
1. New User Account
2. Select User
3. View Chirps
4. Public Chirp
5. Private Chirp
6. Exit""")
      choice = input("> ")
      # if statements to direct by choice - final else will exit

      # else:
      #   sys.exit()


  # option 1
  def create_user(self):
    # will create new account
    pass

  # option 2
  def select_user(self):
    # will allow current user to select a user to proceed as
    pass

  # option 3
  def view_chirps(self):
    # if user present allow current user to see public and private chirps
    pass

  # option 4
  def write__public_chirps(self):
    # if user present, allow current user to create public chirps
    pass

  # option 5
  def write_private_chirps(self):
    # if user present, allow current user to select another user
    # to write a chirp to
    pass



  # serialze and deserialize section
  def serialze(self):
    pass

  def deserialize(self):
    pass

#example from mathmagician exercise
if __name__ == '__main__':
  birdyboard = Birdyboard()
  birdyboard.show_menu()

# to run - pyhon birdybaord.py