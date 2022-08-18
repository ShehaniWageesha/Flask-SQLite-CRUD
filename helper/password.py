import bcrypt
import random
import string

def hashpw(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def random_pw():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str