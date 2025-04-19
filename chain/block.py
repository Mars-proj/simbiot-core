import hashlib
import json
import time

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.data = data
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "data": self.data
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
