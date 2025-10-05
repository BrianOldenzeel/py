def num_to_binary(n):
    number = n
    binary = ""
    while number > 0:
        remain = number % 2
        number = number // 2  
        binary = str(remain) + binary
    return binary

print(num_to_binary(18))


def num_to_base(n, b):
    if n == 0:
        return ""
    r = ""
    while n > 0:
        r = str(n % b) + r
        n = n // b
    return r

print(num_to_base(42, 5))


assert num_to_base(42, 5) == '132'

def base_b_to_num(s, b):
    total = 0
    for index, i in enumerate(s[::-1]):
        total = (int(i) * pow(b, index)) + total

    return total

print(base_b_to_num("132", 4))
print(base_b_to_num("101010", 2))

assert base_b_to_num("101010", 2) == 42