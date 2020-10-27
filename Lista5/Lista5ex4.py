linhas = int(input())
quant_p = quant_u = 0

for _ in range(linhas):
    frase = input().lower()
    quant_p += frase.count('p')
    quant_u += frase.count('u')
print(f'{quant_p} {quant_u}')
