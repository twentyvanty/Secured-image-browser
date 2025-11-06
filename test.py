from cryptography.fernet import Fernet, InvalidToken
import base64
from pathlib import Path

def generate_key():
    """Generates a Fernet key and saves it to a file."""
    key_file_path = Path("filekey.key")
    if not key_file_path.exists():
        key = Fernet.generate_key()
        with open("filekey.key", "wb") as key_file:
            key_file.write(key)
        print("Key has been generated and saved.")
    else:
        print("Key file already exists. Using existing key.")
    
def encrypt_image(image_file, key_file):
    """Encrypts an image file using a given key."""
    # Load the key from the key file
    with open(key_file, "rb") as k_file:
        key = k_file.read()
    
    # Initialize the Fernet cipher suite
    fernet = Fernet(key)
    
    # Read the original image data in binary mode
    with open(image_file, "rb") as f:
        image_data = f.read()
    
    # Encrypt the image data
    encrypted_data = fernet.encrypt(image_data)
    
    # Write the encrypted data to a new file
    with open('locked_img.png', 'wb') as locked_photo_file:
        locked_photo_file.write(encrypted_data)
    
    print("Image encrypted successfully and saved ")

def decrypt_image(encrypted_image_file, key_file):
    """Decrypts an encrypted image file using a given key."""
    # Load the key from the key file
    with open(key_file, "rb") as k_file:
        key = k_file.read()
    
    # Initialize the Fernet cipher suite
    fernet = Fernet(key)
    
    # Read the encrypted image data in binary mode
    with open(encrypted_image_file, "rb") as ef:
        encrypted_data = ef.read()
    
    # Decrypt the image data
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Write the decrypted data to a new file
    with open("unlock_image.png", "wb") as output_file:
        output_file.write(decrypted_data)
    
    print("Image decrypted successfully and saved.")

if __name__ == "__main__":
    generate_key()
    # encrypt_image("sample.png", "filekey.key")
    # decrypt_image("locked_img.png", "filekey.key")
    # image ="locked_img.png"
    image ="sample.png"
    
    try:
        decrypt_image(image, "filekey.key")
    except InvalidToken:
        encrypt_image(image, "filekey.key")
