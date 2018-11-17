from bcrypt import gensalt, hashpw
from hashlib import sha256
from base64 import b64encode

def gen_salt():
    return gensalt()


def hashpw(plain, salt):
    return hashpw(b64encode(sha256(plain.encode()).digest()), salt)


def check(plain, salt, hashed):
    return hash(plain, salt) == hashed
