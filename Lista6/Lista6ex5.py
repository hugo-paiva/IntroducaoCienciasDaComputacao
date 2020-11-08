tamanho = int(input())

matriz = []
coluna = 0
linha_local = 0
for _ in range(tamanho):
    linha = input().split()
    matriz.append(linha)
matriz_final = matriz[:]
for num_coluna in range(tamanho):
    for num_linha in range(tamanho -1, -1, -1):
        if matriz[num_linha][num_coluna] == '.':
                if matriz[linha][num_coluna] == 'o':
                    matriz_final[linha][num_coluna] = '.'
                    matriz_final[num_linha][num_coluna] = 'o'
for linha in matriz_final:
    for item in linha:
        print(item, end=' ')
    print()




'''for num_linha, linha in enumerate(matriz):
    for num_coluna, simbol in enumerate(linha):
        if simbol =='o':
            coluna = num_coluna
            linha_local = num_linha
            if matriz_final[linha_local+1][coluna] == '.':
                matriz_final[linha_local+1][coluna] = 'o'
                matriz_final[linha_local][coluna] = '.' '''