def fechou_loop(inicial, atual):
    if atual >= len(caderneta) or atual < 0: return ''
    if caderneta[atual]['indice'] == inicial:
        return caderneta[atual]['nome']
    return fechou_loop(inicial, caderneta[atual]['indice'])


ganhador = ''
caderneta = []

for inicio in range(int(input())):
    nome, idx = input().split()
    caderneta += [{'nome': nome, 'indice': int(idx)-1}]
    if not ganhador:
        ganhador = fechou_loop(inicio,inicio)

print(ganhador)



"""
num_jogadas = int(input())
registro_jogadas = []
jogador = {}
for _ in range(num_jogadas):
    jogador['nome'], jogador['proximo'] = input().split()
    registro_jogadas.append(jogador.copy())
for j in registro_jogadas:
    if j['proximo'] == str(num_jogadas):
def getNome():

    getNome(j['proximo'])"""