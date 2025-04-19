import hashlib
import time
import uuid
from wallet import Wallet
import json
import os

class GenesisBlock:
    def __init__(self):
        self.timestamp = time.time()
        self.creator_wallet = Wallet()
        self.block_id = str(uuid.uuid4())
        self.data = {
            "block_id": self.block_id,
            "timestamp": self.timestamp,
            "creator_address": self.creator_wallet.address,
            "creator_private_key": self.creator_wallet.private_key
        }
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.data, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def save(self):
        if not os.path.exists("data"):
            os.mkdir("data")
        with open("data/genesis_block.json", "w") as f:
            json.dump({
                "hash": self.hash,
                "data": self.data
            }, f, indent=4)

if __name__ == "__main__":
    genesis = GenesisBlock()
    genesis.save()
    print("Genesis-блок создан.")
    print("Hash:", genesis.hash)
    print("Кошелёк Создателя:", genesis.creator_wallet.address)
