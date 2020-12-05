num_movimentos = int(input())
coord = {'N': 0, 'S': 0, 'L': 0, 'O': 0}

for _ in range(num_movimentos):
    direcao, quadras = input().split()
    coord[direcao] += int(quadras)

vert, horiz = min(coord['N'], coord['S']), min(coord['L'], coord['O'])
coord['N'] -= vert
coord['S'] -= vert
coord['L'] -= horiz
coord['O'] -= horiz

print(coord['S'], coord['N'], coord['O'], coord['L'],)
