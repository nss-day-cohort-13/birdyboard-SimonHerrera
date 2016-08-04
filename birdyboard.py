import csv
import os
import sys
import pickle
import time
import uuid

class Birdyboard:

  def __init__(self):
    """ Initialization

    """
    self.new_user = {}
    self.current_user = None
    self.all_users = [] # list of all users
    try:
      self.deserialize_users() # runs this
    except EOFError:
      self.all_users = []
    # pass

  def show_menu(self):
    """ Show main menu and allow for option selection

    """
    clear = lambda: os.system('cls')
    clear()

    while True:
      self.page_clear()
      print('This is the current user: ', self.current_user)
      time.sleep(.3)
      print("""  #########################################
  ##           Birdyboard~~~~~           ##
  #########################################
  1. New User Account
  2. Select User
  3. View Chirps
  4. Public Chirp
  5. Private Chirp
  6. Exit""")
      choice  = input(" Select an option: > ")
      try:
        choice = int(choice)
      except Exception:
        self.main_menu_invalid_input()
        continue

      if choice == 1:
        self.page_clear()
        print('You have chosen to create a new account')
        full_name = input('Type in your desired Full Name: ')
        user_name = input('Type in your desired User Name: ')
        self.current_user = self.create_user(full_name, user_name)
      elif choice == 2:
        self.select_user()
      elif choice == 3:
        if not self.current_user:
          self.main_menu_invalid_input()
        else:
          self.view_chirps()
      elif choice == 4:
        if not self.current_user:
          self.main_menu_invalid_input()
        else:
          self.write_public_chirps()
      elif choice == 5:
        if not self.current_user:
          self.main_menu_invalid_input()
        else:
          self.write_private_chirps()
      elif choice == 6:
        sys.exit()
      else:
        self.main_menu_invalid_input()


  def main_menu_invalid_input(self):
    """ This reloads the main menu if current user is not set

    """
    print('This is not a valid selection - please try again')
    time.sleep(1.5)
    clear = lambda: os.system('cls')
    clear()

  def select_user_invalid_input(self):
    """ This reloads the select user menu if no valid option is selected

    """
    print('This is not a valid selection - please try again')
    time.sleep(1.5)
    clear = lambda: os.system('cls')
    clear()


  def page_clear(self):
    """ This clears the page when called

    """
    clear = lambda: os.system('cls')
    clear()


  def list_users(self):
    """ This lists and adds a number to allow for user selection

    """
    count = 1
    for user in self.all_users:
      print(str(count) + '. ' + user[2])
      count = count + 1


  def create_user(self, full_name, user_name):
    """ This is used to create a new user

    """

    # Create and gather info to append to all_users
    newuid = uuid.uuid4()
    self.all_users.append([newuid, full_name, user_name])
    # Welcome new user
    print('Welcome: {}'.format(user_name))
    time.sleep(1.5)
    self.serialize_users()
    return user_name


  def select_user(self):
    """ Allows user to select the active user

    """
    # will allow current user to select a user to proceed
    if self.all_users == []:
      print('Currently no users exist, please Create a new user')
      time.sleep(1.5)
      self.show_menu()
    else:

      while True:
        self.page_clear()
        print('List of Users')
        self.list_users()
        selected = input("Pick a User? > ")

        try:
          selected = int(selected)
        except Exception:
          self.select_user_invalid_input()
          continue

        if (selected >= 1) & (selected <= len(self.all_users)):
          try:
            # print('len', len(self.all_users))
            # print('selected ', selected)
            # print('selected ', self.all_users[3][2])
            # print('all users ', self.all_users)
            self.current_user = self.all_users[selected-1][2]
            print('Welcome: ', self.current_user)
            time.sleep(1.5)
            break
          except Exception:
            self.select_user_invalid_input()
            continue
        else:
          self.select_user_invalid_input()

      self.show_menu()

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


  def serialize_users(self):
    """ wb+ w/r write to file

    """
    with open('users.txt', 'wb+') as file:
      pickle.dump(self.all_users, file)


  def deserialize_users(self):
    """ rb+ w/r load on initialization

    """
    try:
      with open('users.txt', 'rb+') as file:
        self.all_users = pickle.load(file)
    except FileNotFoundError: # Raised when a file or directory is requested but doesn’t exist
      self.all_users = []

      return self.all_users


if __name__ == '__main__':
  birdyboard = Birdyboard()
  birdyboard.show_menu()

# to run - python birdybaord.py