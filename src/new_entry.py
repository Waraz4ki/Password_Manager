from encryption import file_encryptor

title = input("Title: ")
username = input("Username: ")
password = input("Password: ")

def write_entry(save_file):
    with open(save_file, "a") as file:
        file.write(title+username+password)


write_entry("moritz.kd")
file_encryptor.encrypt_file("moritz.kd", "data/encryption_key.key")


    
    
    