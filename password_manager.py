import random
import string
password={}
try:
    with open("passwords.txt","r") as file:
        for line in file:
            website,pwd=line.strip().split(":")
            passwords[website]=pwd
            
except:
    pass
def generate_password():
    chars=string.ascii_letters+ string.digits+"!@#$%&*"
    password="".join(random.choice(chars) for _ in range(8))
    return password
while True:
    print("\n----PASSWORD MANAGER----")
    print("1. save password")
    print("2. view passwords")
    print("3. generate password")
    print("4. Exit")

    choice=input("enter your choice=")
    if choice=="1":
        site=input("enter website=")
        pwd=input("enter password")
        password[site]=pwd
        with open("passwords.txt","a") as file:
            file.write(f"{site} : {pwd}\n")
        print("saved!!")
    elif choice=="2":
        if not password:
            print("no data!!")
        else:
            for site ,pwd in password.items():
                print(site ,":", pwd)
    elif choice=="3":
        print("generated password=", generate_password)
    elif choice=="4":
        print("ok byee!!")
    else:
        print("invalid input!!")
