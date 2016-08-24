import uuid


class Conversation:


    def __init__(self, chirp_uuid):
            self.chirp_list = [chirp_uuid]
            self.conversation_uuid = uuid.uuid4()

    def add_chirp_reply(self, chirp_uuid):
        self.chirp_list.append(chirp_uuid)

if __name__ == '__main__':
  c = Conversation()
