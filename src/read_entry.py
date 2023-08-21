from encryption import AES as aes

key_location = "data/key"
AES = aes.AESCipher(key_location)

def read_entries(save_file):
    with open(save_file, "r")as file:
        AES.decrypt(file.read())
        #! Figure out why only the first input get's returned
        
read_entries("data/moritz.kd")
