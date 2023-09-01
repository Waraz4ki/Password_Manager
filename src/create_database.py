from encryption import AES as aes


key_location = "data/key"
AES = aes.AESCipher(key_location)

database = input("")
master_key = AES.encrypt(input(""))

with open(database, "w", encoding="utf-8") as file:
    file.writelines(master_key)
    
