import uuid


class Conversation:


    def __init__(self, chirp_uuid):
            self.chirp_list = []
            self.conversation_uuid = uuid.uuid4()
            self.chirp_list[0] = chirp_uuid # set index 0 to chirp uuid

if __name__ == '__main__':
  c = Conversation()