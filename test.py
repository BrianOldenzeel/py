from random import choice # import the function choice from the module named random
import sys



user = input()
comp = choice(["steen", "papier", "schaar"])

if user != "steen" and user != "papier" and user != "schaar":
    sys.exit(1)

print("De gebruiker (jij) koos", user)
print("De computer (ik) koos", comp)

if user == comp:
    print("Gelijk spel")
elif user == "steen" and comp == "schaar":
    print("EZ WIN voor " + user)
elif user == "papier" and comp == "steen":
    print("EZ WIN voor " + user)
elif user == "schaar" and comp == "papier":
    print("EZ WIN voor " + user)
else:
    print("verloren jij noob " + user)

