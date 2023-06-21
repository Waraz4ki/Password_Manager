
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("data/encryption_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("data/encryption_key.key", "rb").read()
    
# Encode string to bytes to enrcypt it
def encrypt_string(string):
    encoded_string = string.encode()
    f = Fernet(load_key())
    encryptet = f.encrypt(encoded_string)
    print(encryptet)

encrypt_string("hi")

