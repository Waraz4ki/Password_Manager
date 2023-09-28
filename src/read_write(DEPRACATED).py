from AES import AESCipher

database = ("database.kd")
password = ("Moin")
AES = AESCipher(password=password, database=database)

def write_entry():
    Title = b"Title"
    Name = b"Name"
    Password = b"Password"
    
    AES.encrypt(Title, "ab")
    AES.encrypt(Name, "ab")
    AES.encrypt(Password, "ab")
    
    #with open(database, "wb")as file:
    #    file.write(AES.encrypt(plain_text=Title))
    #    file.write(AES.encrypt(plain_text=Name))
    #    file.write(AES.encrypt(plain_text=Password))
    
def read_entry():
    decrypted_data = AES.decrypt()            

