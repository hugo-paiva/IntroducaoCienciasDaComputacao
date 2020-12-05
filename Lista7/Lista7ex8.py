frase = input()
for s in '.?,!:':
    frase = frase.replace(s , '')
frase = frase.split()
contagem = {}
for idx, palavra in enumerate(frase):
    frase[idx] = palavra.capitalize()
for palavra in frase:
    contagem[palavra] = frase.count(palavra)

ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

lista = []
final = []
cont = anterior = 0
recortar = ordenado.copy()
for item in ordenado:
    if cont == 0:
        anterior = item[1]
    cont += 1
    if item[1] == anterior:
        lista.append(recortar.pop(0))
    if recortar == []:
        lista.sort(reverse=True)
        final += lista
        break
    if item[1] != anterior:
        lista.sort(reverse=True)
        final += lista
        lista = []
        lista.append(recortar.pop(0))
    anterior = item[1]
for i in final: print(i[0], i[1])