from random import choice # import the function choice from the module named random

choices = ["steen", "papier", "schaar", "spock", "hagedis"]

rules = []

user = input("Kies een wapen (steen, papier of schaar): ")


comp = choice(choices)



print("De gebruiker (jij) koos", user)
print("De computer (ik) koos", comp)


