import os
import sys
import pickle
import time
import uuid
from user import *
from chirp import *

class Birdyboard():


  def __init__(self, users_filename, chirps_filename, conversations_filename):
    """ Initialization

    """
    self.users_filename = users_filename
    self.chirps_filename = chirps_filename
    self.conversations_filename = conversations_filename
    self.current_user = None
    self.current_chirp = None
    self.current_conversation = None

    try:
      self.all_users = self.deserialize_data(self.users_filename)
    except EOFError:
      self.all_users = {}
    try:
      self.all_chirps = self.deserialize_data(self.chirps_filename)
    except EOFError:
      self.all_chirps = {}
    try:
      self.all_conversations = self.deserialize_data(self.conversations_filename)
    except EOFError:
      self.all_conversations = {}


  def page_clear(self):
    """ This clears the page when called

    """
    clear = lambda: os.system('cls')
    clear()


  def show_menu(self):
    """ Show main menu and allow for option selection

    """
    while True:
      self.page_clear()
      if not self.current_user:
        print('No Current User')
      else:
        print('Current User: ', self.current_user.user_name)

      print("""  #########################################
  ##           Birdyboard~~~~~           ##
  #########################################
  1. New User Account
  2. Select User
  3. View Chirps
  4. Public Chirp
  5. Private Chirp
  6. Exit""")
      user_choice  = input(" Select an option: > ").lower()

      if user_choice == '1':
        # Create and gather info to append to all_users
        self.page_clear()
        print('You have chosen to create a new account')
        full_name = input('Type in your desired Full Name: ')
        user_name = input('Type in your desired User Name: ')
        self.current_user = self.create_user(full_name, user_name) # this = new_user

      elif user_choice == '2':
        self.select_user()
      elif user_choice == '3':
        self.page_clear()

        self.select_chirp()
      elif user_choice == '4':
        if not self.current_user:
          self.main_menu_invalid_input()
        else:
          self.page_clear()
          print('You have chosen to create a new Public Chirp')
          chirp_message = input('Type your new Chirp: ')
          self.current_chirp = self.create_public_chirp(chirp_message, self.current_user.user_uuid) # this = new_chirp
      elif user_choice == '5':
        if not self.current_user:
          self.main_menu_invalid_input()
        else:
          self.page_clear()
          print('You have chosen to create a new Private Chirp')
          current_receiver = self.select_receiver()
          if current_receiver == None:
            print('There is no receiver')
            self.show_menu()
          else:
            chirp_message = input ('Type your new Chirp: ')
            self.current_chirp = self.create_private_chirp(chirp_message, self.current_user.user_uuid, True, current_receiver)
      elif user_choice == '6':
        sys.exit()
      else:
        self.main_menu_invalid_input()


  def main_menu_invalid_input(self):
    """ This reloads the main menu if current user is not set

    """
    print('This is not a valid selection - please try again')
    time.sleep(1.5)


  def select_user_invalid_input(self):
    """ This reloads the select user menu if no valid option is selected

    """
    print('This is not a valid selection - please try again')
    time.sleep(1.5)
    clear = lambda: os.system('cls')
    clear()



  def list_users(self):
    """ This lists and adds a number to allow for user selection

    """
    line_count = 1
    user_line_to_uuid = {} #new dict to hold uuid
    for uuid, value in self.all_users.items():
      user_line_to_uuid[str(line_count)] = uuid
      print('{}.  {}'.format(line_count, value.user_name))
      line_count += 1
    return user_line_to_uuid # to select_customer

    ##Old Code
    # count = 1
    # for user in self.all_users:
    #   print(str(count) + '. ' + user[2])
    #   count = count + 1

  def list_chirps(self):
    """ This lists all public chirps as well as chirps the current user is associated with

    """
    line_count = 1
    chirp_line_to_uuid = {} #new dict to hold uuid
    for uuid, value in self.all_chirps.items():
      chirp_line_to_uuid[str(line_count)] = uuid
      print('{}.  {}'.format(line_count, value.chirp_message))
      line_count += 1
    return chirp_line_to_uuid # to select_chirp


  def create_user(self, full_name, user_name):
    """ This is used to create a new user

    """
    new_user = User(full_name, user_name)

    self.all_users[new_user.user_uuid] = new_user
    self.serialize_data(self.all_users, self.users_filename)
    time.sleep(1)
    return new_user

  def select_user(self):
    """ Allows user to select the active user

    """
    # will allow current user to select a user to proceed
    while True:
      self.page_clear()
      print('Select a User')
      if self.all_users == {}:
        print('No users exist, please create a new user')
        time.sleep(1.5)
        return #back to main menu
      else:
        user_line_to_uuid = self.list_users() # returns uuid {line_number: uuid}
        line_number = input("Select a User > ") # line_number = line selected
        if line_number not in user_line_to_uuid:
          print('Not a valid User')
          time.sleep(1)
        else:
          current_uuid = user_line_to_uuid.get(line_number) # get uuid from cu_line_to_uuid
          self.current_user = self.all_users.get(current_uuid) # pass uuid from line = current cust
          return #back to main menu

  def select_receiver(self):
    """ Allows user to select the active user

    """
    # will allow current user to select a receiver of a chirp
    while True:
      self.page_clear()
      if len(self.all_users) == 1:
        print('You are the only user, you cannot send a Chirp to yourself')
        time.sleep(2)
        return None
      else:
        receiver_line_to_uuid = self.list_users() # returns uuid {line_number: uuid}
        line_number = input("Select a Receiver > ") # line_number = line selected
        if line_number not in receiver_line_to_uuid:
          print('Not a valid User')
          time.sleep(1)
        else:
          current_uuid = user_line_to_uuid.get(line_number) # get uuid from cu_line_to_uuid
          return self.all_users.get(current_uuid) # pass uuid from line = current receiver+

        # print('Who are you sending this Chirp to? ')
        # self.list_users()
        # time.sleep(1)
      # return # rec uuid

  def select_chirp(self):
    """ Allows user to select a Chirp to reply to

    """
    # will allow current user to select a Chrip
    while True:
      self.page_clear()
      print('Select a Chirp')
      if self.all_chirps == {}:
        print('No chirps exist, please create a Chirp')
        time.sleep(1.5)
        return #back to main menu
      else:
        chirp_line_to_uuid = self.list_chirps() # returns uuid {line_number: uuid}
        line_number = input("Select a Chirp > ") # line_number = line selected
        if line_number not in chirp_line_to_uuid:
          print('Not a valid Chirp')
          time.sleep(1)
        else:
          current_uuid = chirp_line_to_uuid.get(line_number) # get uuid from cu_line_to_uuid
          self.current_chirp = self.all_chirps.get(current_uuid) # pass uuid from line = current cust
          return #back to main menu

  # option 4
  def create_public_chirp(self, chirp_message, user_uuid):
    # if user present, allow current user to create a public chirp
    """ This is used to create a public chirp

    """
    new_chirp = Chirp(chirp_message, user_uuid)
    # new_chirp.private = True
    # print('show', new_chirp.private)
    # time.sleep(1)

    self.all_chirps[new_chirp.chirp_uuid] = new_chirp
    self.serialize_data(self.all_chirps, self.chirps_filename)
    time.sleep(1)
    return new_chirp


  # option 5
  def create_private_chirp(self, chirp_message, user_uuid, private, receiver):
    # if user present, allow current user to create a private chirp
    """ This is used to create a private chirp

    """
    new_chirp = Chirp(chirp_message, user_uuid, private, receiver)
    print('show pri', new_chirp.private)
    print('show rec', new_chirp.receiver)
    time.sleep(1)


    self.all_chirps[new_chirp.chirp_uuid] = new_chirp
    self.serialize_data(self.all_chirps, self.chirps_filename)
    time.sleep(1)
    return new_chirp


  def serialize_data(self, data, filename):
    """ wb+ w/r write to file
,
    """
    with open(filename, 'wb+') as file:
      pickle.dump(data, file)


  def deserialize_data(self, filename):
    """ rb+ w/r load on initialization

    """
    try:
      with open(filename, 'rb+') as file:
        data = pickle.load(file)
    except FileNotFoundError: # Raised when a file or directory is requested but doesn’t exist
      data = {}

    return data


if __name__ == '__main__':
  birdyboard = Birdyboard('users.p', 'chirps.p', 'conversations.p')
  birdyboard.show_menu()

# to run - python birdyboard.py