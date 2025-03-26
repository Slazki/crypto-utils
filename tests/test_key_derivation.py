import pytest
from crypto_utils.key_derivation import derive_key_argon2

def test_derive_key_argon2():
    password = "testpassword"
    salt = b"12345678"  # Not secure, just for test
    key = derive_key_argon2(password, salt, length=16)
    assert len(key) == 16, "Derived key should match the specified length."
