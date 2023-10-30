from cryptography.fernet import Fernet
import os


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("secret.key", "rb").read()


def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message


while __name__ == "__main__":
    if not os.path.isfile("secret.key"):
        print("No encryption key found. Please generate a key first.")
        choice = '1'
    else:
        choice = input("Choose an option (1: Generate Key, 2: Encrypt, 3: Decrypt): ")

    if choice == '1':
        generate_key()
        print("Key generated and saved as 'secret.key'.")
    elif choice == '2':
        key = load_key()
        message = input("Enter the message to encrypt: ")
        encrypted_message = encrypt_message(message, key)
        print("Encrypted message:", encrypted_message.decode())
    elif choice == '3':
        key = load_key()
        encrypted_message = input("Enter the encrypted message: ")
        decrypted_message = decrypt_message(encrypted_message.encode(), key)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please choose 1 to generate a key, 2 for encryption, or 3 for decryption.")
