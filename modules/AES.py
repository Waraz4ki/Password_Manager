import hashlib
import secrets

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad



class AESCipher:
    def __init__(self, password, database):
        #salt = secrets.token_bytes(32) <-- maybe find a way to generate a salt using the password
        self.database = database
        salt = b'\xe9\xe2>\x84l\x99\x0cB\xefC\xf8w\x07C\xdd\x80\xdb\xd9\x96\xa3\xb28\x8dM\x03\xf7\xeb\x84\x84\x99\xd9\xbf'
        self.key = PBKDF2(password, salt, dkLen=32)
        
    def encrypt(self, plain_text):
        cipher = AES.new(self.key, AES.MODE_CBC) #<-- This is the line that knows everything I don't know
        seperator = b":"
        encrypted_data = cipher.encrypt(pad(b"start:" + plain_text + b":end", AES.block_size))
        
        with open(self.database, "ab") as file:
            file.write(cipher.iv)
            file.write(encrypted_data)
        

    def decrypt(self):
        with open(self.database, "rb") as file:
            iv = file.read(16)
            data = file.read()
            
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv) #<-- This is the line that knows everything I don't know
        original = unpad(cipher.decrypt(data), AES.block_size).split(b":")
        del original[::2]
        print(original)
