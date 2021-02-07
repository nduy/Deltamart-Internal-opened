import binascii
import random
import string

def get_rand_string(length):
    letters = string.ascii_uppercase
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

