import string
import random

def id_generator(size=6, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

pssw = "Aa@0"
while True:
    p = id_generator(4)

    print(p)

    if p==pssw:
        print(f"Password is: {p}")
        break
    
