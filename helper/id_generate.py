import random

def generate_pin(n=5):
    digits = ""
    for i in range(n):
        digits += str(random.randint(0, 9))
    return digits