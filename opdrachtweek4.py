import random

# opdracht 1

def power(b, p):
    result = 1
    for x in range(p):
        result = result * b
    return result

print(power(2, 5))

#
# Tests voor de lus-versie van machtsverheffen
#
assert power(2, 5) == 32
assert power(5, 2) == 25
assert power(42, 0) == 1
assert power(0, 42) == 0
assert power(0, 0) == 1


# opdracht 2

def summed_odds(list):
    result = 0
    for x in list:
        if x % 2 == 0:
            result = result
        else:
            result = result + x
    return result


# tests!
assert summed_odds([4, 5, 6]) == 5
assert summed_odds(range(3, 10)) == 24


def unique(L):
    """Returns whether all elements in L are unique.

    Argument: L, a list of any elements.
    Return value: True, if all elements in L are unique,
            or False, if there is any repeated element
    """
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return unique(L[1:])  # in deze functie mag je WEL recursie gebruiken!

# opdracht 3
def until_reapeat(high):
    l = []
    while unique(l):
        guesscount = random.choice(range(0, high))
        l.append(guesscount)
    return guesscount

print(until_reapeat(36))