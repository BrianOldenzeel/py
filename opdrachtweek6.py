def num_to_binary(n):
    number = n
    binary = ""
    while number > 0:
        remain = number % 2
        number = number // 2  
        binary = str(remain) + binary
    return binary

print(num_to_binary(18))

# opdracht 1

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

# opdracht 2

def base_b_to_num(s, b):
    total = 0
    for index, i in enumerate(s[::-1]):
        total = (int(i) * pow(b, index)) + total

    return total

print(base_b_to_num("203", 4))
print(base_b_to_num("101010", 2))

assert base_b_to_num("101010", 2) == 42

def base_to_base(b1, b2, s_in_b1):
    total = 0
    r = ""
    for index, i in enumerate(s_in_b1[::-1]):
        total = (int(i) * pow(b1, index)) + total
    while total > 0:
        r = str(total % b2) + r
        total = total // b2
    return r

print(base_to_base(2, 10, "11"))
print(base_to_base(2, 3, "101010"))

def add(s, t):
    return num_to_binary(int(s, 2) + int(t, 2))

print(add("11100", "11110"))
assert add("11100", "11110") == '111010'