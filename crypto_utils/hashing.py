import hashlib

def sha256_hash(data: bytes) -> bytes:
    """
    Returns the SHA-256 digest of the input data.
    
    :param data: Data to hash (bytes)
    :return: SHA-256 digest (bytes)
    """
    hasher = hashlib.sha256()
    hasher.update(data)
    return hasher.digest()
