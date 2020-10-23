valor = input()
cont_percurssos = 0
somatorio = 0
consumo_max = 0
while valor.strip().lower() != 'final':
    valor = int(valor)
    cont_percurssos += 1
    if cont_percurssos == 1:
        consumo_max = valor
    if valor > consumo_max:
        consumo_max = valor
    somatorio += valor

    valor = input()

print(f'{consumo_max} {somatorio/cont_percurssos:.1f}', end=' ')
if (100 - somatorio) < 10:
    print('reserva')
