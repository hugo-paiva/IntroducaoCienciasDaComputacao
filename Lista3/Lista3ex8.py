num = 1
cont = soma = maior = 0
while num != 0:
  num = int(input())
  if num == 0:
    break
  if cont == 0:
    maior = num
  cont += 1
  if num > maior:
    maior = num
  soma += num
print(cont)
print(maior)
if cont == 0:
  cont = 1
print(f'{soma/cont:.2f}')
