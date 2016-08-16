import uuid


class Chirp:


    def __init__(self, chirp_message, user_uuid, private=False, receiver=None):
            self.chirp_message = chirp_message
            self.user_uuid = user_uuid
            self.private = private
            self.receiver = receiver
            self.chirp_uuid = uuid.uuid4()

if __name__ == '__main__':
  c = Chirp()