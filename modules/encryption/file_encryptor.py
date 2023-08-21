from cryptography.fernet import Fernet


# Create/Modify a Key
def write_key(key_dir):
    key = Fernet.generate_key()
    with open(key_dir, "wb") as key_file:
        key_file.write(key)

# Load a created key using Parameters
def load_key(key):
    return open(key, "rb").read()

# Encrypt files using the Parameter 
def encrypt_file(data, used_key):
    f = Fernet(load_key(used_key))
    
    with open(data, "rb") as file:
        file_data = file.read()

    token = f.encrypt(file_data)

    with open(data, "wb") as file:
        file.write(token)

# Decrypt files using the Parameter
def decrypt_file(data, used_key):
    f = Fernet(load_key(used_key))
    
    with open(data, "rb") as file:
        file_data = file.read()
        
    encryptet_data = f.decrypt(file_data)

    with open(data, "wb") as file:
        file.write(encryptet_data)
