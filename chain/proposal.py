import uuid

class Proposal:
    def __init__(self, title, description, action):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.action = action
