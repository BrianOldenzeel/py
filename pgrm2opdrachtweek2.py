def plusone(n):
    """Geeft n terug door 1-en op te tellen!
    """
    if n == 0:  # base case
        return 0
    else:       # recursive case
        return 1 + plusone(n-1)

assert plusone(0) == 0  # test de base case
assert plusone(5) == 5  # test de oplossing


def pow(b, p):
    """b**p, recursief!
    """
    if p == 0:  # base case
        return 1.0
    else:       # recursive case
        return b * pow(b, p-1)

def keepvwl(s):
    """Geef ALLEEN de klinkers in s terug
    """
    if s == "":
        return ""
    elif s[0] in "aeiou":
        vwl = ""
        return s[0] + keepvwl(s[1:])
    else:
        return keepvwl(s[1:])

print(keepvwl("halen"))

def max(L):
    """Geef de grootste waarde van L terug
    """
    if len(L) == 1:
        return L[0]
    
    M = max(L[1:])  # De max van het RESTANT van L
    
    if L[0] > M:
        return L[0]
    else:
        return M

print(max([7, 5, 9, 2]))


def no_doubles(L):
    if len(L) == 1:
        return L

    if L[0] not in L[1:]:
        return L[:1] + no_doubles(L[1:])
    else:
        return no_doubles(L[1:])

print(no_doubles([1, 2, 3, 3, 4, 5]))
print(no_doubles("test"))


def fact(number, counter=1):
    if counter > number:
        return []

    if number % counter == 0:
        return [counter] + fact(number, counter + 1)
    else:
        return fact(number, counter + 1)

print(fact(32))


def mult(n, m):

    if m == 0:
        return 0
    else:
        return n + mult(n, m-1)

print(mult(6, 3))

def dot(L, k):
    
    if len(L) != len(k):
        return 0.0
    
    if len(L) == 0:
        return 0.0
    
    return L[0] * k[0] + dot(L[1:], k[1:])

print(dot([5, 3], [6, 4]))

def ind(e, l):
    
    if len(l) == 0:
        return 0
    
    if e == l[0]:
        return 1 + ind(e, l[1:])
    else: 
        return ind(e, l[1:])

print(ind(42, [55, 77, 42, 12, 42, 100]))

print(ind('hoi', ['oh', 'hoi', 'daar']))

def letter_score(let):
    if let in "adenirsto":
        return 1
    if let in "q":
        return 10
    if let in "uvwjk":
        return 4
    if let in "xy":
        return 8
    if let in "bcmp":
        return 3
    if let in "ghl":
        return 2
    if let in "f":
        return 5
    if let in "z":
        return 6


def scrabble_score(s):
    
    if s == "":
        return 0

    return letter_score(s[0]) + scrabble_score(s[1:])

print(scrabble_score('quotums'))
print(scrabble_score('pyjama'))



def transcribe(s):
    
    if s == "":
        return ""
    
    if s[0] == "A":
        return "U" +transcribe(s[1:])
    elif s[0] == "C":
        return "G" + transcribe(s[1:])
    elif s[0] == "G":
        return "C" + transcribe(s[1:])
    elif s[0] == "T":
        return "A" + transcribe(s[1:])
    else:
        return transcribe(s[1:])

print(transcribe('ACGT TGCA'))
print(transcribe('GATTACA'))
print(transcribe('hallo'))