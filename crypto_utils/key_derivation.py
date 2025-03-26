from argon2.low_level import hash_secret_raw, Type

def derive_key_argon2(password: str, salt: bytes, length: int = 32) -> bytes:
    """
    Derive a cryptographic key from a password using Argon2id.
    
    :param password: The password (str).
    :param salt: A random, unique salt (bytes).
    :param length: Desired key length in bytes (default 32 = 256-bit).
    :return: The derived key (bytes).
    """
    # Adjust memory_cost, time_cost, parallelism as desired.
    key = hash_secret_raw(
        secret=password.encode("utf-8"),
        salt=salt,
        time_cost=2,
        memory_cost=102400,
        parallelism=8,
        hash_len=length,
        type=Type.ID
    )
    return key
