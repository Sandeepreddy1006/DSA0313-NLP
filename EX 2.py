def fsa_match(s):
    state = 0
    for char in s:
        if state == 0:
            state = 1 if char else 0
        if state == 1:
            state = 2 if char == 'a' else 1
        if state == 2:
            state = 3 if char == 'b' else (2 if char == 'a' else 1)
    return state == 3

print(fsa_match("cab"))   # True
print(fsa_match("abc"))   # False
