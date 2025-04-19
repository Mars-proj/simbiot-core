from cryptography.fernet import Fernet
import os

class SecureKeyManager:
    def __init__(self, key_file="../secrets/simbiot.key", cipher_file="../secrets/simbiot.key.enc"):
        self.key_file = key_file
        self.cipher_file = cipher_file
        self.master_key_path = "../secrets/.master.key"
        self.fernet = None
        self._load_or_create_master_key()

    def _load_or_create_master_key(self):
        if os.path.exists(self.master_key_path):
            with open(self.master_key_path, "rb") as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self.master_key_path, "wb") as f:
                f.write(key)
        self.fernet = Fernet(key)

    def encrypt_key(self):
        with open(self.key_file, "rb") as f:
            data = f.read()
        encrypted = self.fernet.encrypt(data)
        with open(self.cipher_file, "wb") as f:
            f.write(encrypted)
        os.remove(self.key_file)

    def decrypt_key(self):
        with open(self.cipher_file, "rb") as f:
            encrypted = f.read()
        decrypted = self.fernet.decrypt(encrypted)
        return decrypted.decode("utf-8")
