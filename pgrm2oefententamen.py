def check_extension(s, e):
    if e == "":
        return True
    
    if s == "":
        return False

    if e[-1] != s[-1]:
        return False

    return check_extension(s[:-1], e[:-1])

assert check_extension("tentamen.docx", ".exe") == False
assert check_extension("program.exe", ".exe") == True
assert check_extension("wk8ex1.py", ".py") == True

def only_even_loop(l):
    res = []
    for item in l:
        if item % 2 == 0:
            res.append(item)
    return res
assert only_even_loop([0, 1, 2, 3, 4]) == [0, 2, 4]

def only_even_lc(l):
    res = [item for item in l if item % 2 == 0]
    assert only_even_lc([0, 1, 2, 3, 4]) == [0, 2, 4]

def only_even_rec(l):
    if len(l) == 0:
        return l

    if l[0] % 2 == 0:
        return [l[0]] + only_even_rec(l[1:])
    
    return only_even_rec(l[1:])

assert only_even_rec([0, 1, 2, 3, 4]) == [0, 2, 4]

L = [
    ["0308230", 7.6, True],
    ["8273927", 5.1, False],
    ["8234987", 6.4, False],
    ["2368612", 5.9, True],
    ["9731827", 3.2, False],
]
hw = [[item[0], item[1] + 0.5] for item in L if item[2] is True]
print(hw)

def alfabet_word(s):
    if len(s) == 1:
        return True
    
    if s[0] < s[1]:
        return alfabet_word(s[1:]) 

    return False

print(alfabet_word("abc"))
print(alfabet_word("cba"))


def complexity_score(text):
    score_count = 0
    words_split = text.split()
    word_count = len(words_split)
    sentence_split = text.split(".")[:-1]
    sentence_count = len(sentence_split)

    for word in words_split:
        if len(word) > 10:
            score_count += 1

    for sentence in sentence_split:
        if len(sentence.split()) > 15:
            score_count += 1
    
    return (score_count / (word_count + sentence_count)) * 100

print(complexity_score(
            "Dit is een gecompliceerde zin met veel verschillende woorden erin verstopt."
        ))

assert round(complexity_score("Dit is een korte zin."), 1) == 0.0
# Uitleg:
# Woorden (5): Dit(1) is(2) een(3) korte(4) zin(5)
# Zinnen (1): 1 zin van 5 woorden (< 15, dus niet complex)
# Score: 0 complexe elementen / 6 totale elementen = 0.0%

assert (
    round(
        complexity_score(
            "Dit is een gecompliceerde zin met veel verschillende woorden erin verstopt."
        ),
        1,
    )
    == 16.7
)
# Uitleg:
# Woorden (11): Dit(1) is(2) een(3) gecompliceerde(4) zin(5) met(6) veel(7)
#               verschillende(8) woorden(9) erin(10) verstopt(11)
# Zinnen (1): 1 zin van 11 woorden (< 15, dus niet complex)
# Complex: gecompliceerde(13 letters), verschillende(13 letters)
# Score: 2 complexe woorden / 12 totale elementen ≈ 16.7%

assert (
    round(complexity_score("De intelligentie van computerprogramma's neemt toe."), 1)
    == 28.6
)
# Uitleg:
# Woorden (6): De(1) intelligentie(2) van(3) computerprogramma's(4)
#              neemt(5) toe(6)
# Zinnen (1): 1 zin van 6 woorden (< 15, dus niet complex)
# Complex: intelligentie(12 letters), computerprogramma's(16 letters)
# Score: 2 complexe woorden / 7 totale elementen ≈ 28.6%

assert (
    round(
        complexity_score("Programmeren is leuk. Dit is een zeer lange zin die meer dan vijftien woorden bevat en daarom als complex wordt beschouwd bij deze analyse. Nog een zin."),
        1,
    )
    == 6.7
)
# Uitleg:
# Zin 1 (3): Programmeren(1) is(2) leuk(3)
# Zin 2 (21): Dit(1) is(2) een(3) zeer(4) lange(5) zin(6) die(7) meer(8) dan(9)
#             vijftien(10) woorden(11) bevat(12) en(13) daarom(14) als(15)
#             complex(16) wordt(17) beschouwd(18) bij(19) deze(20) analyse(21)
# Zin 3 (3): Nog(1) een(2) zin(3)
# Complex: programmeren(11 letters), en zin 2 (21 woorden > 15)
# Score: 2 complexe elementen / 30 totale elementen ≈ 6.7%