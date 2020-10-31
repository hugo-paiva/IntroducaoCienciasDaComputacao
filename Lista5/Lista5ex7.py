frase = input()
for caractere in frase:
    if caractere.isupper():
        print('U', end='')
    elif caractere.islower():
        print('L', end='')
    elif caractere.isspace():
        print('W', end='')
    elif caractere.isnumeric():
        print('D', end='')
