# Python Encryption Script

This Python script provides a simple command-line interface for generating encryption keys and performing message encryption and decryption using the Fernet symmetric key encryption algorithm.

## Features

- **Generate Encryption Key**: You can generate a secure encryption key using the script, and it will be saved to a file named `secret.key`.

- **Encrypt a Message**: With the encryption key in place, you can encrypt any message of your choice. The script will prompt you to enter the message, and it will provide you with the encrypted version of the message.

- **Decrypt an Encrypted Message**: If you have an encrypted message and the encryption key, you can use the script to decrypt the message and view the original content.

## Usage

1. **Generate Encryption Key**:
   - When you run the script for the first time, choose option 1 to generate an encryption key.
   - The generated key will be saved to a file named `secret.key`.

2. **Encrypt a Message**:
   - With a pre-existing encryption key, choose option 2 to encrypt a message.
   - Enter the message you want to encrypt when prompted.
   - The script will provide you with the encrypted message.

3. **Decrypt an Encrypted Message**:
   - If you have an encrypted message and the encryption key, choose option 3 to decrypt the message.
   - Enter the encrypted message when prompted.
   - The script will display the decrypted message.

## Important
- Ensure that the encryption key file (`secret.key`) is kept secure and not shared, as it is required for decryption.
- This script provides basic data security and privacy for your messages. For more robust encryption needs, consider using professional encryption tools and libraries.

## Requirements

- Python 3.6 or higher.
- `cryptography` library. You can install it using `pip install cryptography`.

## License

This script is released under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to contribute and improve this script. Your contributions are welcome!
