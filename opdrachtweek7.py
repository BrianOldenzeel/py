def next(term):
    term_string = str(term)
    final = ""
    temp = 1

    for index in range(1, len(term_string)):
        if term_string[index] == term_string[index - 1]:
            temp += 1
        else:
            final += str(temp) + term_string[index - 1]
            temp = 1
        
    final += str(temp) + term_string[-1]

    return int(final)

print(next(21))
print(next(312211))
assert next(21) == 1211
assert next(2222) == 42  # merk op dat dit getal niet voorkomt in de echte rij
assert next(312211) == 13112221



def read_it(n):
    number = str(1)
    final = ""
    temp = 1

    for i in range(n):
        number = next(number)
        print(number)

read_it(6)