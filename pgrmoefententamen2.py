def check_extension(s, e):
    if e == "":
        return True

    if s == "":
        return False
    
    if s[-1] != e[-1]:
        return False 
    
    return check_extension(s[:-1], e[:-1])
    

assert check_extension("tentamen.docx", ".exe") == False
assert check_extension("program.exe", ".exe") == True
assert check_extension("wk8ex1.py", ".py") == True

def only_even_loop(L):
    res = []
    for i in L:
        if i % 2 == 0:
            res.append(i)
    return res
assert only_even_loop([0, 1, 2, 3, 4]) == [0, 2, 4]

def only_even_lc(L):
    res = [item for item in L if item % 2 == 0]
    return res

assert only_even_lc([0, 1, 2, 3, 4]) == [0, 2, 4]

def only_even_rec(L):
    if len(L) == 0:
        return L

    if L[0] % 2 == 0:
        return [L[0]] + only_even_rec(L[1:])

    return only_even_rec(L[1:])

assert only_even_rec([0, 1, 2, 3, 4]) == [0, 2, 4]
L = [
    ["0308230", 7.6, True],
    ["8273927", 5.1, False],
    ["8234987", 6.4, False],
    ["2368612", 5.9, True],
    ["9731827", 3.2, False],
]

HW = [[item[0], item[1] + 0.5] for item in L if item[2] == True]
print(HW)
