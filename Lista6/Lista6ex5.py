tamanho = int(input())

matriz = []
for _ in range(tamanho):
    matriz.append(input().split())
for num_linha_base in range(tamanho -1, 0, -1):
    for num_coluna_base in range(tamanho):
        if matriz[num_linha_base][num_coluna_base] == '.': 
            for elevacao_obj in range(num_linha_base -1, -1, -1):
                if matriz[elevacao_obj][num_coluna_base] == 'x': # Testa se há obstáculo, caso haja quebra o loop e passa pra coluna seguinte
                    break
                if matriz[elevacao_obj][num_coluna_base] == 'o':
                    matriz[num_linha_base][num_coluna_base] = 'o'
                    matriz[elevacao_obj][num_coluna_base] = '.'
                    break
for linha in matriz:
    for item in linha:
        print(item, end=' ')
    print()




'''for num_linha, linha in enumerate(matriz):
    for num_coluna, simbol in enumerate(linha):
        if simbol =='o':
            coluna = num_coluna
            linha_local = num_linha
            if matriz[linha_local+1][coluna] == '.':
                matriz[linha_local+1][coluna] = 'o'
                matriz[linha_local][coluna] = '.' '''