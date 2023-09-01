from AES import AESCipher

database = "database"
AES = AESCipher(password="master_key", database=database)


def write_entry():
    Title = b"Title"
    Name = b"Name"
    Password = b"Password"
    
    AES.encrypt(plain_text=Title)
    AES.encrypt(plain_text=Name)
    AES.encrypt(plain_text=Password)
    
def read_entry():
    decrypted_data = AES.decrypt()
    
    
write_entry()
read_entry()
