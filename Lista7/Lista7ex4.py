num_jogadas = int(input())
registro_jogadas = []
jogador = {}
for _ in range(num_jogadas):
    jogador['nome'], jogador['proximo'] = input().split()
    registro_jogadas.append(jogador.copy())
for j in registro_jogadas:
    if j['proximo'] == str(num_jogadas):
def getNome():

    getNome(j['proximo'])