valor, parcelas = input().split()
valor, parcelas = [float(valor), int(parcelas)]
if parcelas == 1:
    valorFinal = valor * 0.95
elif parcelas == 2:
    valorFinal = valor
elif parcelas == 3:
    valorFinal = valor * 1.05
elif parcelas == 4:
    valorFinal = valor * 1.1
print(f'{valorFinal:.2f} {valorFinal/parcelas:.2f}')
