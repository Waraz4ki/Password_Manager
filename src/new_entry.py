from encryption import AES as aes

key_location = "data/key"
AES = aes.AESCipher(key_location)

Title = AES.encrypt(input(""))
Name = AES.encrypt(input(""))
Password = AES.encrypt(input(""))

def write_entry(save_file):
    with open(save_file, "a") as file:
        file.write(Title)
        file.write(Name)
        file.write(Password)

write_entry("data/moritz.kd")