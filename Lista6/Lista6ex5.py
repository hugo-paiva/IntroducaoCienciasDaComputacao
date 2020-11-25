tamanho = int(input())

matriz = []
for _ in range(tamanho):
    matriz.append(input().split())
for num_linha in range(tamanho -1, 0, -1):
    for num_coluna in range(tamanho):
        bloco = matriz[num_linha][num_coluna]
        if bloco == '.':
            vizinho = matriz[num_linha-1][num_coluna]
            if vizinho == 'o':
                matriz[num_linha][num_coluna] = 'o' # Bloco recebe 'o'
                matriz[num_linha-1][num_coluna] = '.' # Vizinho recebe '.'

for linha in matriz:
    for item in linha:
        print(item, end=' ')
    print()
