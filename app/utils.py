import hashlib

def hash_password(password):
    """Gera hash SHA256 da senha"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed):
    """Verifica se a senha corresponde ao hash"""
    return hash_password(password) == hashed
