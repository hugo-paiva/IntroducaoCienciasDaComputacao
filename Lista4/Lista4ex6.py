def mmc(maior, x, y):
    if maior % x == 0 and maior % y == 0:
        return maior
    else:
        return mmc(maior + 1, x, y)
    

def mdc(a, b):
    menor = a
    if b < a: menor = b
    for c in range(1, menor + 1):
        if a % c == 0 and b % c == 0:
            MDC = c
    return MDC


while True:
    a, b = input().split()
    a, b = int(a), int(b)

    if a < 0 or b < 0:
        break
    if a == 0 or b == 0:
        print(0)
        continue

    #MDC para usado reduzir o numero de recursões na função mmc
    MDC = mdc(a, b)

    #Caso especial mmc com número primo (quando maior divisor comum(MDC) é igual a 1)
    if MDC == 1:
        print(a*b)
        continue

    maior_num = a
    if b > maior_num:
        maior_num = b
    
    #Simplicando valores com MDC
    maior_num /= MDC
    a /= MDC
    b /= MDC

    print(int(mmc(maior_num, a, b) * MDC)) # Multiplica o resultado final pelo mdc
