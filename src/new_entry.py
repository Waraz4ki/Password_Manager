

title = input("Title: ")
username = input("Username: ")
password = input("Password: ")
                
with open("data\data", "a") as file:
    file.write(title+username+password)

    
    
    