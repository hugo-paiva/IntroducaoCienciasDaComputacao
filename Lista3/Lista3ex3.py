n = int(input())
for c in range(n):
  x, y = input().split()
  x, y = [int(x), int(y)]
  if x % 2 == 0:
    x += 1
  somaImpares = 0
  for num in range(x, x + 2*y, 2):
      somaImpares += num
  if c == 0:
    maior = menor = somaImpares
  if somaImpares > maior:
    maior = somaImpares
  if somaImpares < menor:
    menor = somaImpares
  print(somaImpares)
print(maior)
print(menor)
media = (maior + menor)/2
print(f'{media:.2f}')
