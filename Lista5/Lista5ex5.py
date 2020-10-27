frase = input()
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
        print(caractere, end='')
