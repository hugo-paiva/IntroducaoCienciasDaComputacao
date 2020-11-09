def hanoi_iterativo(discos, A, B, C, passos):
    cont = 0
    if len(A) % 2 == 0:
        while len(C) != discos:
            if len(B) == 0 or A[-1] < B[-1]:
                B.append(A.pop())
                cont += 1
                if cont == passos:
                    return 0
            elif len(A) == 0 or B[-1] < A[-1]: # Do contrário faço o movimento inverso
                A.append(B.pop())
                cont += 1
                if cont == passos:
                    return 0

            if len(C) == 0 or A[-1] < C[-1]:
                C.append(A.pop())
                cont += 1
                if cont == passos:
                    return 0
            elif len(A) == 0 or C[-1] < A[-1]: # Do contrário faço o movimento inverso
                A.append(C.pop())
                cont += 1
                if cont == passos:
                    return 0

            if len(C) == 0 or B[-1] < C[-1]:
                C.append(B.pop())
                cont += 1
                if cont == passos:
                    return 0
            elif len(B) == 0 or C[-1] < B[-1]: # Do contrário faço o movimento inverso
                B.append(C.pop())
                cont += 1
                if cont == passos:
                    return 0

    if len(A) % 2 != 0:
        while len(C) != discos:
            if len(C) == 0 or A[-1] < C[-1]:
                C.append(A.pop())
                cont += 1
                if cont == passos:
                    return 0
            elif len(A) == 0 or C[-1] < A[-1]: # Do contrário faço o movimento inverso
                A.append(C.pop())
                cont += 1
                if cont == passos:
                    return 0

            if len(B) == 0 or A[-1] < B[-1]:
                B.append(A.pop())
                cont += 1
                if cont == passos:
                    return 0
            elif len(A) == 0 or B[-1] < A[-1]: # Do contrário faço o movimento inverso
                A.append(B.pop())
                cont += 1
                if cont == passos:
                    return 0

            if len(C) == 0 or B[-1] < C[-1]:
                C.append(B.pop())
                cont += 1
                if cont == passos:
                    return 0
            elif len(B) == 0 or C[-1] < B[-1]: # Do contrário faço o movimento inverso
                B.append(C.pop())
                cont += 1
                if cont == passos:
                    return 0


discos, passos = input().split()
discos, passos = int(discos), int(passos)
A = list(range(discos, 0, -1))
B = []
C = []
hanoi_iterativo(discos, A, B, C, passos)
print(len(A), len(B), len(C), sep=' ')