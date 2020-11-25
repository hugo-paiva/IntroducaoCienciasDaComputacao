num_palavras = int(input())
dicio = {}
lista_palavras = []
for _ in range(num_palavras):
    dicio['palavra'], dicio['comportamento'] = input().split()
    lista_palavras.append(dicio.copy())
frase = input().split()
resultado = []
for p in frase:
    for gatilho in lista_palavras:
        if p == gatilho['palavra']:
            resultado.append(gatilho['comportamento'])

if resultado != []:
    print(' '.join(resultado))
else:
    print('Tudo bem!')
