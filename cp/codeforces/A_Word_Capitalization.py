def capitalize_word(word):
    pass
    fw= word[0]
    cw=""
    cfl= fw.upper()
    cw+=cfl
    for letter in word[1:]:
        cw+=letter
    return cw


word = input()
print(capitalize_word(word))