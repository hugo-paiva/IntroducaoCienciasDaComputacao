valor = int(input())
print(valor)
for cedula in [100, 50, 20, 10, 5, 2, 1]:
    print(f'{valor//cedula} nota(s) de R$ {cedula},00')
    valor %= cedula
