import hashlib
import uuid

class Wallet:
    def __init__(self):
        self.private_key = self._generate_private_key()
        self.address = self._generate_address(self.private_key)

    def _generate_private_key(self):
        return str(uuid.uuid4()) + str(uuid.uuid4())

    def _generate_address(self, private_key):
        return hashlib.sha256(private_key.encode()).hexdigest()
