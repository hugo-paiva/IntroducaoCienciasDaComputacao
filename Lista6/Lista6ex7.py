'''count = 0
a = []
b = []
c = []
def hanoi(n,source,target,spare, step_count):
    global count, a, b, c
    if n > 0:
        hanoi(n-1, source, spare, target, step_count)
        target.append(source.pop())
        count = count + 1
        if count == step_count:
            a = A[:]
            b = B[:]
            c = C[:]
        hanoi(n-1, spare, target, source, step_count)

discos, passos = input().split()
discos, passos = int(discos), int(passos)
A = list(range(1, discos + 1))
B = []
C = []
hanoi(discos, A, C, B, passos)
print(len(a), len(b), len(c), sep=' ')'''


