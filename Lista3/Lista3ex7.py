n = int(input())
termo_atual = 1
termo_anterior = 0
cont = 2

if n == 1 or n == 2:
  seq = 1

else:
  while cont <= n:
    seq = termo_atual + termo_anterior
    termo_anterior = termo_atual
    termo_atual = seq
    cont += 1

fatorial = x = 1
for _ in range(n):
  fatorial *= x
  x += 1

print(f'{seq} {fatorial}', end='')
if seq % 2 == 0:
  mes_seguinte = termo_atual + termo_anterior - seq
  print(f' {mes_seguinte}')