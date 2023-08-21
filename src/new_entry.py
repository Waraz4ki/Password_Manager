from encryption import file_encryptor
from cryptography.fernet import Fernet

encoding = "utf-8"
key = "lxp0wlS5yygvg2jyl1AS3toNKvhewzhulAmMMPyj0Co="

encrypt = Fernet(key).encrypt

title = encrypt((input("Title: ").encode(encoding)))
print(Fernet(key).decrypt(title))
username = encrypt((input("Name: ").encode(encoding)))
password = encrypt((input("Pass: ").encode(encoding)))


def write_entry(save_file):
    with open(save_file, "a") as file:
        file.write(title.decode(encoding))
        file.write(username.decode(encoding))
        file.write(password.decode(encoding))



    
    
    