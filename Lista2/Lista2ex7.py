p = float(input())
h = float(input())
imc = p/h**2
print(f'{imc:.2f}')
if imc < 18.5:
  print('Baixo peso')
elif imc < 24.9:
  print('Peso normal')
elif imc < 29.9:
  print('Sobrepeso')
elif 29.9 <= imc < 34.9:
  print('Obesidade grau I')
elif 34.9 <= imc < 39.9:
  print('Obesidade grau II')
elif imc >= 39.9:
  print('Obesidade grau III')

if imc > 24.9:
  precisaPerder = p - 24.9 * h**2
  print('{:.2f}'.format(precisaPerder))
