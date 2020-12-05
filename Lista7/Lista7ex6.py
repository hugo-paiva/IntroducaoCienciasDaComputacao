num_palavras = int(input())

lista_gatilhos = {}
for _ in range(num_palavras):
    gatilho, comportamento = input().split()
    lista_gatilhos[gatilho] = comportamento
    
frase = input().split()
resultado = []
for palavra in frase:
    for gatilho, comportamento in lista_gatilhos.items():
        if palavra == gatilho:
            resultado.append(comportamento)

if resultado != []:
    print(' '.join(resultado))
else:
    print('Tudo bem!')
