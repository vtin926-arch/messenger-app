from cryptography.fernet import Fernet
import base64

# Generate a key for encryption (in production, use a secure key)
def generate_key():
    return Fernet.generate_key()

def encrypt_message(message: str, key: bytes) -> str:
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message: str, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(encrypted_message.encode()).decode()