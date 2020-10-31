"""frase = input()
passou_do_ponto = False

for index, caractere in enumerate(frase):
    if index == 0:
        print(frase[0].upper(), end='')
        continue
    if caractere == '.':
        passou_do_ponto = True
    if passou_do_ponto and caractere not in ' .':
        print(caractere.upper(), end='')
        passou_do_ponto = False
    else:
        print(caractere, end='')"""

import string

frase = input()
capitalizar = True
frase_final = ''
for letra in frase:
    if capitalizar and letra in string.ascii_letters:
        frase_final += letra.upper()
        capitalizar = False
    else:
        frase_final += letra
    if letra == '.':
        capitalizar = True
print(frase_final)