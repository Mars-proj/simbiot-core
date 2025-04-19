from block import Block
import json
import os

class SimbiotChain:
    def __init__(self):
        self.chain = []
        self.load_chain()

    def create_genesis_block(self):
        genesis_data = {
            "message": "Genesis Block",
            "creator": "SIMBIOTCHAIN"
        }
        genesis_block = Block(0, "0", genesis_data)
        self.chain.append(genesis_block)

    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), last_block.hash, data)
        self.chain.append(new_block)

    def load_chain(self):
        if os.path.exists("data/chain.json"):
            with open("data/chain.json", "r") as f:
                loaded = json.load(f)
                for block in loaded:
                    self.chain.append(Block(
                        block["index"],
                        block["previous_hash"],
                        block["data"]
                    ))
        else:
            self.create_genesis_block()

    def save_chain(self):
        if not os.path.exists("data"):
            os.mkdir("data")
        with open("data/chain.json", "w") as f:
            json.dump([{
                "index": block.index,
                "timestamp": block.timestamp,
                "previous_hash": block.previous_hash,
                "data": block.data,
                "hash": block.hash
            } for block in self.chain], f, indent=4)
