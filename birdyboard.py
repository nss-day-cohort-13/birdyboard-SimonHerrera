import csv
import os
import sys
import pickle
import time

class Birdyboard:

  def __init__(self):
    pass

  def show_menu(self):
    clear = lambda: os.system('cls')
    clear()

    while True:
      # Main loop, for use in getting function we want to run, must be 1-6
      print("""  #########################################
  ##           Birdyboard~~~~~           ##
  #########################################
  1. New User Account
  2. Select User
  3. View Chirps
  4. Public Chirp
  5. Private Chirp
  6. Exit""")
      # choice = int(input(" Select an option: > "))
      choice  = input(" Select an option: > ")
      try:
        choice = int(choice)
      except Exception:
        self.main_menu_invalid_input()
        continue

      # if statements to direct by choice - final else will exit
      if choice == 1:
        self.create_user()
      elif choice == 2:
        self.select_user()
      elif choice == 3:
        view_chirps()
      elif choice == 4:
        write_public_chirps()
      elif choice == 5:
        write_private_chirps()
      elif choice == 6:
        sys.exit()
      else:
        self.main_menu_invalid_input()


  def main_menu_invalid_input(self):
    print('This is not a valid selection - please try again')
    time.sleep(1.5)
    clear = lambda: os.system('cls')
    clear()


  # option 1
  def create_user(self):
    # will create new account
    print('You have chosen to create a new account')
        # screen_name = input(">")
        # current_user = screen_name
    pass

  # option 2
  def select_user(self):
    # will allow current user to select a user to proceed as
    pass

  # option 3
  def view_chirps(self):
    # if user present allow current user to see public and private chirps
    # csv example below used on a practice exercise I did (save here for now)
    # with open ('chirps.csv') as csvfile:
    #     readCSV = csv.reader(csvfile, delimiter=',') # splits on comma or cell
    pass

  # option 4
  def write_public_chirps(self):
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