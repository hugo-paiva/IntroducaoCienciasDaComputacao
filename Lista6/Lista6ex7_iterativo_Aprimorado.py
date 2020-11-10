def vazio(pino):
    if pino == []:
        return True
    return False


def pode_mover(x, y):
    if vazio(y) or not vazio(x) and x[-1] < y[-1]:
        y.append(x.pop())
        return True


cont = 0
def verificar_que_terminou(passos):
    global cont, discos
    cont += 1
    if cont == passos or len(C) == discos:
        return True
    return False


def hanoi_iterativo(discos, A, B, C, passos):
    if len(A) % 2 == 0:
        while True:

            if pode_mover(A, B) or pode_mover(B, A): # Tentamos o movimento em ambas direções
                if verificar_que_terminou(passos): return

            if pode_mover(A, C) or pode_mover(C, A): # Tentamos o movimento em ambas direções
                if verificar_que_terminou(passos): return

            if pode_mover(B, C) or pode_mover(C, B): # Tentamos o movimento em ambas direções
                if verificar_que_terminou(passos): return

    else:
        while True:

            if pode_mover(A, C) or pode_mover(C, A): # Tentamos o movimento em ambas direções
                if verificar_que_terminou(passos): return

            if pode_mover(A, B) or pode_mover(B, A): # Tentamos o movimento em ambas direções
                if verificar_que_terminou(passos): return

            if pode_mover(B, C) or pode_mover(C, B): # Tentamos o movimento em ambas direções
                if verificar_que_terminou(passos): return


discos, passos = input().split()
discos, passos = int(discos), int(passos)
A, B, C = list(range(discos, 0, -1)), [], []
hanoi_iterativo(discos, A, B, C, passos)
print(len(A), len(B), len(C), sep=' ')
