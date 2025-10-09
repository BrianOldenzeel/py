def next(term):
    term_string = str(term)
    final = ""
    temp = 1

    for index in range(1, len(term_string)):
        if term_string[index] == term_string[index - 1]:
            temp += 1
        else:
            final += str(temp) + term_string[index - 1]
            count = 1
        
    final += str(temp) + term_string[-1]

    return final

print(next(21))