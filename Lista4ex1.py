def compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


x = int(input())
y = int(input())
resultado = compare(x, y)
if resultado == 1:
    print('x e maior que y')
elif resultado == -1:
    print('x e menor que y')
else:
    print('x e igual a y')
