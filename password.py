from cryptography.fernet import Fernet
import json
import random
import string
import os

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

if not os.path.exists("key.key"):
    print("Encryption key not found. Generating a new one...")
    generate_key()

key = load_key()
cipher = Fernet(key)

def save_password(service, username, password):
    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}

    encrypted_password = cipher.encrypt(password.encode()).decode()

    passwords[service] = {"username": username, "password": encrypted_password}
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

    print(f"Password for {service} saved successfully!")

def retrieve_password(service):
    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)

        if service in passwords:
            username = passwords[service]["username"]
            encrypted_password = passwords[service]["password"]
            decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
            print(f"\nService: {service}")
            print(f"Username: {username}")
            print(f"Password: {decrypted_password}\n")
        else:
            print(f"No password found for {service}")
    except FileNotFoundError:
        print("No passwords stored yet!")

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")
    return password

def authenticate():
    master_password = "viceblanka" 
    user_input = input("Enter the master password: ")
    if user_input != master_password:
        print("Authentication failed!")
        exit()
    print("Authentication successful!")

def main():
    authenticate()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Save Password")
        print("2. Retrieve Password")
        print("3. Generate Password")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password (or leave blank to generate): ")
            if not password:
                password = generate_password()
            save_password(service, username, password)
        elif choice == "2":
            service = input("Enter the service name: ")
            retrieve_password(service)
        elif choice == "3":
            generate_password()
        elif choice == "4":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

from cryptography.fernet import Fernet

from cryptography.fernet import Fernet



