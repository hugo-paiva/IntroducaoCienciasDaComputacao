movimentos = int(input())
norte_sul = leste_oeste = 0
for _ in range(movimentos):
    direcao, quadras = input().split()
    quadras = int(quadras)
    if direcao == 'N':
        norte_sul += quadras
    elif direcao == 'S':
        norte_sul -= quadras
    elif direcao == 'L':
        leste_oeste += quadras
    else:
        leste_oeste -= quadras
if norte_sul > 0:
    S = norte_sul
else: S = 0
if norte_sul < 0:
    N = abs(norte_sul)
else: N = 0
if leste_oeste > 0:
    O = leste_oeste
else: O = 0
if leste_oeste < 0:
    L = abs(leste_oeste)
else: L = 0

print(N, S, L, O)
