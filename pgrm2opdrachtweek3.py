def exact_change(t, l):
    if t == 0:
        return True
    if len(l) == 0:
        return False
    if t < 0:
        return False    


    if exact_change(t - l[0], l[1:]):
        return True

    if exact_change(t, l[1:]):
        return True
    
    return False

assert exact_change(100, [5, 5, 5, 10, 10, 25, 50]) == True # 5 + 10 + 10 + 25 + 50
assert exact_change(120, [5, 5, 5, 10, 10, 25, 50]) == False # 5 + 5 + 5 +10 + 10 + 25 + 50 = 110
assert exact_change(32, [1, 5, 5, 10, 10, 25, 50]) == False # 25 + 5 + 1 = 31. 32 is niet mogelijk.
assert exact_change(42, []) is False # er zijn geen munten ...
assert exact_change(0, [5, 5]) is True # er is geen bedrag te betalen ...


def num_coins(t, l):
    if t == 0:
        return 0
    if len(l) == 0:
        return 0
    if t < 0:
        return 0

    first = num_coins(t - l[0], l[1:])
    if first > 0 or t - l[0] == 0:
        return 1 + first

    skip_first = num_coins(t, l[1:])
    if skip_first > 0:
        return skip_first

    
    return 0

    
print(num_coins(100, [5, 5, 5, 10, 10, 25, 50]))

assert num_coins(100, [5, 5, 5, 10, 10, 25, 50]) == 6 # 5 + 10 + 10 + 25 + 50
assert num_coins(120, [5, 5, 5, 10, 10, 25, 50]) == 0 # 5 + 5 + 5 +10 + 10 + 25 + 50 = 110
assert num_coins(32, [1, 5, 5, 10, 10, 25, 50]) == 0 # 25 + 5 + 1 = 31. 32 is niet mogelijk.
assert num_coins(0, [5, 5]) == 0
assert num_coins(42, []) == 0


def nijlpaard_diner(social_distance, loc_diner):
    if len(loc_diner) == 0:
        return 0
    
    if loc_diner[0] - social_distance >= social_distance:
        return 1 + nijlpaard_diner(social_distance, loc_diner[1:])

    return nijlpaard_diner(social_distance, loc_diner[1:])

print(nijlpaard_diner(1, [3,2,3] ))