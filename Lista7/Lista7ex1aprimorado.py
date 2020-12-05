N = int(input())

problemas = []
for i in range(N):
    problema, solucao, dificuldade = input().split()
    problemas.append((int(dificuldade), solucao))


#def funcao(a):
#    return a[0]

problemas.sort(key= lambda a: a[0], reverse=True)

temp = [item[1] for item in problemas]
print(''.join(temp))