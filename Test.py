from cryptography.fernet import Fernet

# Generate a secret key
key = Fernet.generate_key()

def encrypt_email(email):
    f = Fernet(key)
    encrypted_email = f.encrypt(email.encode())
    return encrypted_email

def decrypt_email(encrypted_email):
    f = Fernet(key)
    decrypted_email = f.decrypt(encrypted_email).decode()
    return decrypted_email

# Example usage
encrypted = encrypt_email("example@example.com")
print("Encrypted email:", encrypted)

decrypted = decrypt_email(encrypted)
print("Decrypted email:", decrypted)
print(key)