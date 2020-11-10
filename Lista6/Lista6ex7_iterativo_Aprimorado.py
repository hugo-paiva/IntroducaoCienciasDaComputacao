def pode_mover(x, y):
    if y == [] or x != [] and x[-1] < y[-1]:
        y.append(x.pop())
        return True

def verificar_que_terminou(passos):
    global cont, discos
    cont += 1
    if cont == passos or len(C) == discos:
        return True
    return False

def hanoi_iterativo(discos, a, b, c, passos):
    global cont
    cont = 0
    if len(a) % 2 == 0:
        while True:

            if pode_mover(a, b) or pode_mover(b, a): # Tentamos o movimento em ambas direções
                if verificar_que_terminou(passos): return

            if pode_mover(a, c) or pode_mover(c, a): # Tentamos o movimento em ambas direções
                if verificar_que_terminou(passos): return

            if pode_mover(b, c) or pode_mover(c, b): # Tentamos o movimento em ambas direções
                if verificar_que_terminou(passos): return

    else:
        while True:

            if pode_mover(a, c) or pode_mover(c, a): # Tentamos o movimento em ambas direções
                if verificar_que_terminou(passos): return

            if pode_mover(a, b) or pode_mover(b, a): # Tentamos o movimento em ambas direções
                if verificar_que_terminou(passos): return

            if pode_mover(b, c) or pode_mover(c, b): # Tentamos o movimento em ambas direções
                if verificar_que_terminou(passos): return

discos, passos = input().split()
discos, passos = int(discos), int(passos)

A, B, C = list(range(discos, 0, -1)), [], []
hanoi_iterativo(discos, A, B, C, passos)
print(len(A), len(B), len(C), sep=' ')
