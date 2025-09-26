# Voer deze cel uit
e = [2, 7, 1]
pi = [3, 1, 4, 1, 5, 9]

# Voorbeeldopgave lists, resultaat: [2, 7, 5, 9]
answer0 = e[0:2] + pi[-2:]
print(answer0)

# Opgave 1: Maak de lijst [7, 1]
answer1 = e[1:2] + pi[1:2]
print(answer1)

# Opgave 2: Maak de lijst [1, 1, 2]
answer2 = pi[1], pi[3], e[0]
print(answer2)

# Opgave 3: Maak de lijst [1, 4, 1, 5, 9]
answer3 = pi[1:3], pi[3], pi[4:6]
print(answer3)

# Opgave 4: Maak de lijst [1, 2, 3, 4, 5]
answer4 = e[2], e[0], pi[0], pi[2], pi[4]
print(answer4)

# Voer deze cel uit
h = "hanze"
s = "hogeschool"
g = "groningen"


# Opgave 6: Maak de string 'schoenen' (Ons record: 4 bewerkingen)
answer6 = s[4:8] + g[7:9] + g[7:9]
print(answer6)
