import os
from Cryptodome.Cipher import AES
from Cryptodome import Random

KEY = b'this is a 16 key'  # Replace this or load from env/secure file
BLOCK_SIZE = AES.block_size

def encrypt_data(data: bytes, key: bytes = KEY) -> bytes:
    iv = Random.new().read(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return iv + cipher.encrypt(data)

def decrypt_data(data: bytes, key: bytes = KEY) -> bytes:
    iv = data[:BLOCK_SIZE]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(data[BLOCK_SIZE:])

def encrypt_file(path: str, key: bytes = KEY) -> str:
    with open(path, 'rb') as f:
        plain_data = f.read()

    encrypted_data = encrypt_data(plain_data, key)

    output_path = path + ".bin"
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)

    return output_path

def decrypt_file(path: str, key: bytes = KEY) -> str:
    with open(path, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = decrypt_data(encrypted_data, key)

    output_path = path.replace(".bin", ".dec")
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)

    return output_path

def encrypt_dir(directory: str, key: bytes = KEY, exclude_ext=('.py', '.bin')):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(exclude_ext):
                continue
            file_path = os.path.join(root, file)
            try:
                encrypted = encrypt_file(file_path, key)
                print(f"Encrypted: {file_path} -> {encrypted}")
            except Exception as e:
                print(f"Failed to encrypt {file_path}: {e}")

def decrypt_dir(directory: str, key: bytes = KEY):
    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith('.bin'):
                continue
            file_path = os.path.join(root, file)
            try:
                decrypted = decrypt_file(file_path, key)
                print(f"Decrypted: {file_path} -> {decrypted}")
            except Exception as e:
                print(f"Failed to decrypt {file_path}: {e}")
