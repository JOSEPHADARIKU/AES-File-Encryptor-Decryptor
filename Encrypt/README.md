# 🔐 AES File Encryptor & Decryptor

A full-featured Python project to **encrypt and decrypt files or directories** using AES (CFB mode). Ideal for keeping sensitive data secure.

## 🚀 Features

- 🔒 AES-128 encryption (CFB mode)
- 📁 Encrypts and decrypts files or entire directories
- ⚠️ Skips `.py` and already encrypted `.bin` files
- 🧠 Smart CLI: encrypt by default, decrypt with `--decrypt`
- ✅ Modular, clean codebase — ready for GitHub/production

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 💻 Usage

### 🔐 Encrypt a file or directory:
```bash
python main.py path/to/your/file_or_folder
```

### 🔓 Decrypt a file or directory:
```bash
python main.py path/to/your/encrypted_file_or_folder --decrypt
```

Encrypted files get a `.bin` extension. Decrypted files get a `.dec` extension.

---

## ✅ Requirements

- Python 3.7+
- `pycryptodome`

---

---

## 👤 Author

Created by **Joseph Adariku** 🚀
