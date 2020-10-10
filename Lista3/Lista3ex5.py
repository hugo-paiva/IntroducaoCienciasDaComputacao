qtd_BH = int(input())

somatorio_bacias = 0

for c in range(qtd_BH):
  nome, area, verao, outono, inverno, primavera = input().split()
  area, verao, outono, inverno, primavera = [
                                                float(area),
                                                float(verao),
                                                float(outono),
                                                float(inverno),
                                                float(primavera)
  ]
  indice_pluviometrico = verao + outono + inverno + primavera
  somatorio_bacias += area

  if c == 0:
    maior_valor = menor_valor = indice_pluviometrico
    nome_maior = nome_menor = nome
    menor_estacao = verao

  for estacao in [verao, outono, inverno, primavera]:
    if estacao < menor_estacao: menor_estacao = estacao

  if indice_pluviometrico > maior_valor:
    maior_valor, nome_maior = indice_pluviometrico, nome

  if menor_estacao < menor_valor:
    menor_valor, nome_menor = menor_estacao, nome

print(nome_maior)
print(nome_menor)
print(f'{somatorio_bacias / qtd_BH:.2f}')