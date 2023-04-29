import fileinput

from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb")as key_file:
        key_file.write(key)

        write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close
    return key

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            web, user, passw = data.split("|")
            print("Website: ",web, "| User:",user, "| Password:", passw)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    website = input("Website: ")

    with open('passwords.txt', 'a') as f:
        f.write(website + "|" + name + "|" + pwd + "\n")


while True:

    mode = input("Would you like to add a new password or view existing ones? (view, new), press q to quit" ).lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Option")
    continue