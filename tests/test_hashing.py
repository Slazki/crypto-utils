import pytest
from crypto_utils.hashing import sha256_hash

def test_sha256_hash():
    data = b"hello"
    digest = sha256_hash(data)
    # SHA-256 of 'hello' is known
    known_digest_hex = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    assert digest.hex() == known_digest_hex, "SHA-256 hash mismatch."
