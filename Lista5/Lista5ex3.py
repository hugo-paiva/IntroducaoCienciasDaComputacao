palavra_A, palavra_B = input().lower().split()
palavras = []
palavras.append(palavra_A)
palavras.append(palavra_B)
palavras.sort()
if palavras[1] == palavra_A: # Ganha a palavra que vem depois
    print('A')
else:
    print('B')
