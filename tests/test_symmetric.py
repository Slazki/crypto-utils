import pytest
from crypto_utils.symmetric import aes_encrypt, aes_decrypt

def test_aes_gcm_encryption_decryption():
    key = b"0123456789ABCDEF0123456789ABCDEF"  # 32 bytes for AES-256
    plaintext = b"Test AES GCM"
    
    nonce, ciphertext, tag = aes_encrypt(key, plaintext)
    decrypted = aes_decrypt(key, nonce, ciphertext, tag)
    
    assert decrypted == plaintext, "Decrypted text does not match the original plaintext."
