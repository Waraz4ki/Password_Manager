import hashlib
import secrets

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    def __init__(self):
        salt = b'\xe9\xe2>\x84l\x99\x0cB\xefC\xf8w\x07C\xdd\x80\xdb\xd9\x96\xa3\xb28\x8dM\x03\xf7\xeb\x84\x84\x99\xd9\xbf'
        #self.database = database
        #self.key = PBKDF2(password, salt, dkLen=32)
        
    def encrypt_text(self, password, plaint_text):
        salt = b'\xe9\xe2>\x84l\x99\x0cB\xefC\xf8w\x07C\xdd\x80\xdb\xd9\x96\xa3\xb28\x8dM\x03\xf7\xeb\x84\x84\x99\xd9\xbf'
        key = PBKDF2(password, salt, dkLen=32)
        
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_data = cipher.encrypt(pad(plaint_text, AES.block_size))
        return encrypted_data
    
    def decrypt_text(self, password, encrypted_text):
        salt = b'\xe9\xe2>\x84l\x99\x0cB\xefC\xf8w\x07C\xdd\x80\xdb\xd9\x96\xa3\xb28\x8dM\x03\xf7\xeb\x84\x84\x99\xd9\xbf'
        key = PBKDF2(password, salt, dkLen=32)
    
    def encrypt_to_file(self, password, plain_text, database, wm):
        salt = b'\xe9\xe2>\x84l\x99\x0cB\xefC\xf8w\x07C\xdd\x80\xdb\xd9\x96\xa3\xb28\x8dM\x03\xf7\xeb\x84\x84\x99\xd9\xbf'
        key = PBKDF2(password, salt, dkLen=32)
        
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_data = cipher.encrypt(pad(plain_text, AES.block_size))        
        with open(database, mode=wm) as file:
            file.write(cipher.iv)
            file.write(encrypted_data)

    def decrypt_from_file(self, password, database):
        salt = b'\xe9\xe2>\x84l\x99\x0cB\xefC\xf8w\x07C\xdd\x80\xdb\xd9\x96\xa3\xb28\x8dM\x03\xf7\xeb\x84\x84\x99\xd9\xbf'
        key = PBKDF2(password, salt, dkLen=32)

        with open(database, "rb") as file:
            iv = file.read(16)
            data = file.read()
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        decrypted_data = unpad(cipher.decrypt(data), AES.block_size)
        return decrypted_data
    