import math

def maximum(n1, n2):
    """returns highest value"""
    return max(n1, n2)

print(maximum(3, 20))

def minutes(sec):
    """returns amount of minutes"""
    return sec / 60

print(minutes(360))
assert minutes(360) == 6




#opdracht 1
def tpl(number: int):
    calc = number * 3
    return calc

print("opdracht1")
print(tpl(3))

#opdracht 2a

def min_two(n1: int, n2: int):
    
    return min(n1, n2)

print("opdracht2a")
print(min_two(30,25))

#opdracht 2b

def min_three(n1: int, n2: int, n3: int):
    return min(n1, n2, n3)

print("opdracht2b")
print(min_three(30,25,5))

def absolute(n1: int, n2: int):
    return abs(n1-n2)

print("opdracht3")
print(absolute(20, 30))

#syntax van recusie opdracht 1

def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    x = function(10)


def function(x):
    print(x)
    if x == 0:
        return
    function(x-1)

main()

# opdracht 1a hij telt af van het input cijfer tot 0
# 10 tot en met 0


