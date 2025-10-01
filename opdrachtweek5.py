#
# Voorbeeldprogramma voor een lus voor gebruikersinteractie
#  (een variant van de versie van het college)
#
import math


def menu():
    """A function that simply prints the menu"""
    print()
    print("(0) Voer een nieuwe lijst in")
    print("(1) Druk de huidige lijst af")
    print("(2) Bepaal de gemiddelde prijs")
    print("(3) Bepaal de standaardafwijking")
    print("(4) Bepaal het minimum en de bijbehorende dag")
    print("(5) Bepaal het maximum en de bijbehorende dag")
    print("(6) Je TR-investeringsplan")
    print("(9) Stoppen")



def predict(L):
    min = find_min_loc(L)

    profit = 0

    for i, item in enumerate(L[min[1]:]):
        if(item > min[0]):
            profit = item
    return profit - min[0]


def find_min_loc(L):
    """find min loc uses a loop to return the minimum of L
            and the location (index or day) of that minimum.
        Argument L: a nonempty list of numbers.
        Results:  the smallest value in L, its location (index)
    """
    min_val = L[0]
    min_loc = 0

    for i in list(range(len(L))):
        if L[i] < min_val:  # een kleinere gevonden!
            min_val = L[i]
            min_loc = i

    return min_val, min_loc

def find_max_loc(L):
    max_val = L[0]
    max_loc = 0

    for i in list(range(len(L))):
        if L[i] > max_val:  # een kleinere gevonden!
            max_val = L[i]
            max_loc = i

    return max_val, max_loc


def returnAvg(l):
    total = 0
    for i in l:
        total += i
    
    return total / len(l)

def calcDif(l):
    avg = returnAvg(l)
    squared_diffs = [(x - avg) ** 2 for x in l]
    variance = sum(squared_diffs) / len(l)

    # Standard deviation
    std_dev = math.sqrt(variance)
    return std_dev

def main():
    """The main user-interaction loop"""
    secret_value = 4.2

    L = [30, 10, 20]  # een beginlijst

    while True:     # de lus voor gebruikersinteractie
        print("\n\nDe lijst is", L)
        menu()
        choice = input("Maak een keuze: ")

        #
        # De invoer van de gebruiker "opschonen en controleren"
        #
        try:
            choice = int(choice)   # omzetten naar een int!
        except:
            print("Ik begreep de invoer niet! Verder gaan...")
            continue

        # de gekozen menu-optie uitvoeren
        #
        if choice == 9:    # We willen stoppen
            break          # De hele while-lus afbreken

        elif choice == 0:  # We willen een nieuwe lijst invoeren
            new_L = input("Voer een nieuwe lijst in: ")    # _iets_ invoeren

            #
            # De invoer van de gebruiker "opschonen en controleren"
            #
            try:
                new_L = eval(new_L)   # eval voert de Python-interpreter uit! Let op: Gevaarlijk!
                if not isinstance(new_L, list):
                    print("Dat lijkt geen lijst. L wordt niet aangepast.")
                else:
                    L = new_L  # Hier is het wel OK, dus we passen onze lijst L aan
            except:
                print("Ik begreep de invoer niet. L wordt niet aangepast.")

        elif choice == 1:  # We willen doorgaan...
            continue       # Terug naar het begin van de while-lus

            # laat AVG van de lijst zien
        elif choice == 2:
            print(returnAvg(L))


        elif choice == 3:  # Geheime menu-optoe!
            print(calcDif(L))

        elif choice == 4:  # Nog een geheime menu-optie (nog interessanter...)
            min_val, min_loc = find_min_loc(L)
            print("De kleinste waarde van L is", min_val, "op dag #", min_loc)

        elif choice == 5:  # Geheime menu-optie (iets interessanter...)
            max_val, max_loc = find_max_loc(L)
            print("De grootste waarde van L is", max_val, "op dag #", max_loc)


        elif choice == 6:   # Het volgende element voorspellen en toevoegen
            n = predict(L)  # Het volgende element uit de functie predict halen
            print("Hoogste winst is: ", n)


        else:
            print(choice, " ?      Dat staat niet op het menu!")

    print()
    print("Tot gisteren!")

main()