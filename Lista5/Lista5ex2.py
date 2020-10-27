frase = input()
for letter in frase:
    if letter in 'AEIOUaeiou áéíóú':
        print(letter, end='')
    else:
        print('p',end='')
