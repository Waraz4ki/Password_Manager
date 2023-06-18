

def get_master_key():
    with open("data\data", "r") as file:
        getkey = file.readlines()
        print(getkey[0])

def write_master_key():
    with open("data\data", "a") as file:
        writekey = file.write()
