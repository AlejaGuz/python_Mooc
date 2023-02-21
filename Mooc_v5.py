import string
import random

def id_generatorLetters(size=6, chars=string.ascii_letters):
    return ''.join(random.sample(chars, size))

def id_generatorNumbers(size=6, chars=string.digits):
    return ''.join(random.sample(chars, size))

pssw = "HoLa"
while True:
    p = id_generatorLetters(4)

    print(p)

    if p==pssw:
        print(f"Password is: {p}")
        break

pssw = "3601"
while True:
    p = id_generatorNumbers(4)

    print(p)

    if p==pssw:
        print(f"Password is: {p}")
        break