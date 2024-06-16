import random
import string

def keygen():
    a = ''.join(random.choices(string.ascii_lowercase, k=10))
    print(a)
