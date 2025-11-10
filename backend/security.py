import hashlib
import hmac
import secrets

# Security utils for password hashing and verifying
# Using hashlib.sha256 and salt

def hash_password(password: str, salt: str = None) -> str:
    if salt is None:
        salt = secrets.token_hex(16)
    pwd_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}${pwd_hash}"


def verify_password(password: str, hashed: str) -> bool:
    try:
        salt, pwd_hash = hashed.split('$')
    except ValueError:
        return False
    expected_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    return hmac.compare_digest(expected_hash, pwd_hash)
