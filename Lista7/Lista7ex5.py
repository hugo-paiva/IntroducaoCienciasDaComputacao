num_filosofos = int(input())
dicionario = {}
lutas = {}

for _ in range(num_filosofos):
    identificador, nome_filosofo = input().split()
    dicionario[identificador] = nome_filosofo # guardando o filosofo no

# Lendo lutas e FINISHHIM

(ident, *params) = input().split()
while ident != 'FINISHHIM':
    lutas[ident] = params
    (ident, *params) = input().split()
    atual = params[0]
    
cont = 0
while type(lutas[atual][-1]) == str:
    cont += 1
    atual = lutas[atual][-1]
    if lutas.get(atual) == None:
        break
print(cont)
