opbrengst_tomaten = 150
opbrengst_paprikas = 120
opbrengst_komkommers = 80

totale_opbrengst = opbrengst_komkommers + opbrengst_paprikas + opbrengst_tomaten

omzet_tomaten = opbrengst_tomaten * 3.24
omzet_paprikas = opbrengst_paprikas * 2.87
omzet_komkommers = opbrengst_komkommers * 1.48

totale_omzet = omzet_komkommers + omzet_paprikas + omzet_tomaten

print(totale_omzet, totale_opbrengst)

windspeed = 188

if windspeed >= 209 and windspeed <= 251:
    print('4')
elif windspeed >= 178 and windspeed <= 208:
    print('3')
elif windspeed >= 154 and windspeed <= 177:
    print('2')
elif windspeed >= 119 and windspeed <= 153:
    print('1')
elif windspeed >= 63 and windspeed <= 118:
    print('TS')
elif windspeed <= 62:
    print('TD')
elif windspeed >= 252:
    print('5')


def over_hundred(L):
    """Check if the total of the list is over 100"""
    result = 0
    for i in L:
        result += result + i
    if result > 100:
        return True
    else:
        return False

test = [12,13,14] 
test2 = [12,13,14, 70] 
print(over_hundred(test))

assert over_hundred(test) is False
assert over_hundred(test2) is True

# inp = 0
# pos_number = []
# amount_number = 0
# while inp >= 0:
#     inp = int(input("Geef positief getal: "))
#     if(inp >= 0):
#         amount_number += 1
#         pos_number.append(inp)

# print(sum(pos_number))
# print(amount_number)

def number_stairs(n):
    """makes a stair of the given number"""
    numberstring = ""

    for i in range(1, (n + 1)):
        for number in range(i):
            numberstring += str(number + 1)
        print(numberstring)
        numberstring = ""

number_stairs(5)

def end_check(phrase):
    """
    Bepaalt de langste substring die zowel aan het begin als aan het einde 
    van de string 'phrase' voorkomt, zonder dat deze substrings overlappen.

    Parameters:
        phrase (str): De invoerstring.

    Returns:
        str: De langste substring die zowel aan het begin als het einde voorkomt,
             zonder overlapping. Als er geen overeenkomende substring is, wordt
             een lege string ('') teruggegeven.
    """
    n = len(phrase)
    longest = ""

    # Controleer alle mogelijke lengtes van de prefix/suffix
    for i in range(1, n // 2 + 1):
        if phrase[:i] == phrase[-i:]:
            longest += phrase[:i]

    return longest


# Testgevallen
assert end_check("abXYab") == "ab"       # 'ab' komt aan begin en einde voor
assert end_check("123test123") == "123"        # 'na' is de langste match
assert end_check("abcdef") == ""          # Geen overeenkomst

print("Alle tests geslaagd!")
