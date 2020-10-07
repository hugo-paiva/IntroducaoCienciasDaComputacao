n , m = input().split()
n , m = int(n), int(m)
menor_bloco = n
if m < n: menor_bloco = m
for divisor in range(1, menor_bloco + 1):
  if m % divisor == 0 and n % divisor == 0:
    pilha_MDC = divisor
print(pilha_MDC)
