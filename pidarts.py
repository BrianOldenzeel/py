import random
import math

def throw_dart():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if((x ** 2 + y ** 2) <= 1.0):
        return True

    return False

print(throw_dart())


def for_pi(n):
    hits = 0
    thrown = 0
    for i in range(n):
        thrown += 1
        if(throw_dart() is True):
            hits += 1
        print(hits, ' Raak van ', thrown, ' wopren dus pi is',  4 * (hits/ thrown))
    return 4 * (hits/ thrown)


def while_pi(error):
    hits = 0
    thrown = 0
    diff = 4.0
    while abs(diff - math.pi) > error:
        thrown += 1
        if (throw_dart() is True):
            hits += 1
        print(hits, ' Raak van ', thrown, ' wopren dus pi is',  4 * (hits/ thrown))
        diff = 4 * (hits/ thrown)
    return

while_pi(0.1)