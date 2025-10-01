def num_to_binary(n):
    number = n
    binary = ""
    while number > 0:
        remain = number % 2
        number = number // 2  
        binary = str(remain) + binary
    return binary

print(num_to_binary(18))