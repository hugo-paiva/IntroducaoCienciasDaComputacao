n = int(input())
cont = 0
m = 0
while True:
    m += 1
    num = n*m + 1
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            cont += 1
    if cont != 2:
        print(m)
        break
    else:
        cont = 0
