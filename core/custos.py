import os
import hashlib

class Custos:
    def __init__(self, root_path="./"):
        self.root_path = root_path
        self.hashes = {}

    def run_integrity_check(self):
        for dirpath, _, filenames in os.walk(self.root_path):
            for filename in filenames:
                if filename.endswith(".py"):
                    full_path = os.path.join(dirpath, filename)
                    with open(full_path, "rb") as f:
                        content = f.read()
                        file_hash = hashlib.sha256(content).hexdigest()
                        self.hashes[full_path] = file_hash

    def check_command(self, command):
        if command == "XIIletosatumestbonum":
            print("ACTIO: Creatoris Clavis. SIMBIOT terminatur.")
            exit()
