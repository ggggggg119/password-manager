# Password-manager
password generator, password vault, no fancy security/protection system, basic asf, even my 3 years old cousin could make this

# how to use
<li>install cryptography for encryption (even though is useless in this project)</li>
<li>clone this repo</li>
<li>run python password.py in the terminal and choose what you want to do in the menu by typing the correct number</li>
<li>generate your own key.key file by adding this snippets if it returns an error</li>

<br>

```python
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("New encryption key generated and saved to key.key.")

# Call this function only once so it would not overlaps, delete this when you already run the command once
generate_key()

```
<li>your generated password would be stored in password.json</li>
<li>make sure you change the master password to your own</li>

```python
def authenticate():
    master_password = "viceblanka" #insert your master password here
    user_input = input("Enter the master password: ")
    if user_input != master_password:
        print("Authentication failed!")
        exit()
    print("Authentication successful!")
