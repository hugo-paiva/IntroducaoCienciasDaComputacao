palavra_A, palavra_B = input().lower().split()
if palavra_A > palavra_B: # Ganha a palavra que vem depois, o comando ">" em questão retorna a posição da tabela ASCII e compara
    print('A')
else:
    print('B')
