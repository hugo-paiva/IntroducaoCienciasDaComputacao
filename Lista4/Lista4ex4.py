def quadrado(b):
    return f'{b}^2 = {b**2}'

def eh_par(n):
    if n < 2:
        return ''
    if n % 2 != 0:
        n -= 1
    print(quadrado(n))
    return eh_par(n-2)

def quadrado_de_pares():
    x = 1
    while x != 0:
        x = int(input())
        eh_par(x)


quadrado_de_pares()
