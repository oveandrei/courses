'''hashlib'''

import hashlib

# Hash a string using SHA-256
text = 'secure message'
hashed = hashlib.sha256(text.encode()).hexdigest()
print(hashed) # 64-char hex string

# MD5 (not secure, but useful for checksums)
checksum = hashlib.md5(b"some file content").hexdigest()
print(checksum)


'''hmac'''

import hmac
import hashlib

# Shared secret key
key = b'secret-key'
message = b'important data'

# Generate HMAC with SHA-256
hmac_result = hmac.new(key, message, hashlib.sha256).hexdigest()
print(hmac_result)

# Validate the HMAC
expected = hmac.new(key, message, hashlib.sha256).hexdigest()
if hmac.compare_digest(hmac_result, expected): # hmac.compare_digest() avoids timing attacks - always use it for secure comparison.
    print("Valid HMAC")
else:
    print("Invalid HMAC")


'''secrets'''

import secrets

# Generate a random secure token (hex)
token = secrets.token_hex(16) # 32-character hex string
print(f"Auth token: {token}")

# Generate a secure random number
secure_num = secrets.randbelow(100)
print(f"Random number < 100: {secure_num}" )

# Choose a secure random character from a list
choices = ['red', 'blue', 'green']
print(secrets.choice(choices)) # Random color