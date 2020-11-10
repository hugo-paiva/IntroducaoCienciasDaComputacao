def vazio(letra):
    if letra == []:
        return True
    return False


cont = 0
def verificar_se_terminou(disc, passos):
    global cont
    cont += 1
    if cont == passos or len(C) == disc:
        return True
    return False


def hanoi_iterativo(discos, A, B, C, passos):
    if len(A) % 2 == 0:
        while len(C) != discos:
            if vazio(B) or not vazio(A) and A[-1] < B[-1]:
                B.append(A.pop())
                if verificar_se_terminou(discos, passos): return 0

            elif vazio(A) or not vazio(B) and B[-1] < A[-1]: # Do contrário faço o movimento inverso
                A.append(B.pop())
                if verificar_se_terminou(discos, passos): return 0

            if vazio(C) or not vazio(A) and A[-1] < C[-1]:
                C.append(A.pop())
                if verificar_se_terminou(discos, passos): return 0

            elif vazio(A) or not vazio(C) and C[-1] < A[-1]: # Do contrário faço o movimento inverso
                A.append(C.pop())
                if verificar_se_terminou(discos, passos): return 0

            if vazio(C) or not vazio(B) and B[-1] < C[-1]:
                C.append(B.pop())
                if verificar_se_terminou(discos, passos): return 0

            elif vazio(B) or not vazio(C) and C[-1] < B[-1]: # Do contrário faço o movimento inverso
                B.append(C.pop())
                if verificar_se_terminou(discos, passos): return 0

    if len(A) % 2 != 0:
        while len(C) != discos:
            if vazio(C) or not vazio(A) and A[-1] < C[-1]:
                C.append(A.pop())
                if verificar_se_terminou(discos, passos): return 0

            elif vazio(A) or not vazio(C) and C[-1] < A[-1]: # Do contrário faço o movimento inverso
                A.append(C.pop())
                if verificar_se_terminou(discos, passos): return 0

            if vazio(B) or not vazio(A) and A[-1] < B[-1]:
                B.append(A.pop())
                if verificar_se_terminou(discos, passos): return 0

            elif vazio(A) or not vazio(B) and B[-1] < A[-1]: # Do contrário faço o movimento inverso
                A.append(B.pop())
                if verificar_se_terminou(discos, passos): return 0

            if vazio(C) or not vazio(B) and B[-1] < C[-1]:
                C.append(B.pop())
                if verificar_se_terminou(discos, passos): return 0

            elif vazio(B) or not vazio(C) and C[-1] < B[-1]: # Do contrário faço o movimento inverso
                B.append(C.pop())
                if verificar_se_terminou(discos, passos): return 0


discos, passos = input().split()
discos, passos = int(discos), int(passos)
A, B, C = list(range(discos, 0, -1)), [], []
hanoi_iterativo(discos, A, B, C, passos)
print(len(A), len(B), len(C), sep=' ')
