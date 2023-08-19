import hashlib
import hmac
import base64
import string
import secrets

def is_valid_key(key_string:str):
    if len(key_string) == 0:
        return False
    return True

def generate_unique_string(length=12):
    alphabet = string.ascii_letters + string.digits
    unique_string = ''.join(secrets.choice(alphabet) for _ in range(length))
    return unique_string

def sign_string(secret_key, data):
    signature = hmac.new(secret_key.encode(), data.encode(), 'sha256')
    signature_bytes = signature.digest()
    signature_base64 = base64.b64encode(signature_bytes).decode()
    return signature_base64

def getHash(key_string, secret):
    
    key_start = "-----------Key-Start-----------"
    key_end = "-----------Key-End-----------"
    secret_start="-----------Secret-Start-----------"
    secret_end="-----------Secret-End-----------"
    
    data_to_hash = f"{key_start}{key_string}{key_end}{secret_start}{secret}{secret_end}"
    
    hash_object = hashlib.sha256(data_to_hash.encode())
    verification_hash = hash_object.hexdigest()
    return verification_hash
