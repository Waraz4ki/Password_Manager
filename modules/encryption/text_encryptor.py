
from cryptography.fernet import Fernet

# Create/Modify a Key
def write_key(key_dir):
    key = Fernet.generate_key()
    with open(key_dir, "wb") as key_file:
        key_file.write(key)

# Load a created key using Parameters
def load_key(key):
    return open(key, "rb").read()


# Encode string to bytes to enrcypt it
def encrypt_string(data, used_key):
    encoded_string = data.encode()
    
    f = Fernet(load_key(used_key))

    encryptet = f.encrypt(encoded_string)
    print(encryptet)

