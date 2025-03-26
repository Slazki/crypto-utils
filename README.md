	Crypto Utils

A light cryptography utilities library in Python.  

Provides:
- AES-GCM encryption/decryption
- SHA-256 hashing
- Argon2 password-based key derivation

	Features

1. Symmetric Encryption (AES-GCM)
   - Encrypt and decrypt plaintext with AES in GCM mode.
   - Authenticated encryption ensures data integrity.

2. Hashing
   - Create SHA-256 digests for arbitrary data.

3. Key Derivation (Argon2)
   - Derive strong encryption keys from user passwords.

	Installation

bash
git clone https://github.com/Slazki/crypto-utils.git
cd crypto-utils
pip install -r requirements.txt


Install dependencies:

pip install -r requirements.txt

(Optional)
pip install -e

Running tests to try it out

# if you installed in editable mode:
pytest

# if you didnt install the package, run with Pythons -m flag:
python -m pytest tests

Disclaimer
This code is for educational purposes. If you plan to use these cryptographic routines in production, review best practices, perform thorough security audits, and ensure proper key management.