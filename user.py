import uuid


class User:


    def __init__(self, full_name, user_name):
            self.full_name = full_name
            self.user_name = user_name
            self.user_uuid = uuid.uuid4()

if __name__ == '__main__':
  u = User()