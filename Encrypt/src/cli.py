import argparse
import os
from .encryption import encrypt_file, encrypt_dir, decrypt_file, decrypt_dir

def parse_args():
    parser = argparse.ArgumentParser(description="AES File Encryptor / Decryptor")
    parser.add_argument("path", help="Path to file or directory")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt instead of encrypt")
    return parser.parse_args()

def run():
    args = parse_args()
    path = args.path

    if not os.path.exists(path):
        print("Error: Path does not exist.")
        return

    if args.decrypt:
        if os.path.isfile(path):
            decrypt_file(path)
        elif os.path.isdir(path):
            decrypt_dir(path)
        else:
            print("Unsupported file type for decryption")
    else:
        if os.path.isfile(path):
            encrypt_file(path)
        elif os.path.isdir(path):
            encrypt_dir(path)
        else:
            print("Unsupported file type for encryption")
