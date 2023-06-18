

title = input("Title: ")
username = input("Username: ")
password = input("Password: ")

def write_entry():
    with open("data\data", "a") as file:
        file.write(title+username+password)

    
    
    