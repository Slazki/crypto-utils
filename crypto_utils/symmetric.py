from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def aes_encrypt(key: bytes, plaintext: bytes) -> tuple[bytes, bytes, bytes]:
    """
    Encrypts plaintext using AES in GCM mode.
    
    :param key: Symmetric key (bytes). Should be 16/24/32 bytes (AES-128/192/256).
    :param plaintext: The data to encrypt (bytes).
    :return: (nonce, ciphertext, tag)
    """
    # Generate a random 96-bit nonce for GCM
    nonce = os.urandom(12)
    
    # Create AES-GCM cipher
    cipher = Cipher(
        algorithms.AES(key),
        modes.GCM(nonce),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    
    # Encrypt
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    
    return (nonce, ciphertext, encryptor.tag)

def aes_decrypt(key: bytes, nonce: bytes, ciphertext: bytes, tag: bytes) -> bytes:
    """
    Decrypts AES-GCM ciphertext.
    
    :param key: Symmetric key (bytes).
    :param nonce: The nonce used during encryption.
    :param ciphertext: The encrypted data (bytes).
    :param tag: The authentication tag from encryption.
    :return: Decrypted plaintext (bytes).
    """
    cipher = Cipher(
        algorithms.AES(key),
        modes.GCM(nonce, tag),
        backend=default_backend()
    )
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    return decrypted_data
