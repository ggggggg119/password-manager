# Password-manager
password generator, password vault, no fancy security/protection system, basic asf, even my 3 years old cousin could make this

# how to use
<li>install cryptography for encryption (even though is useless in this project)</li>
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
