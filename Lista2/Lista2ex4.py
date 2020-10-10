a, b = input().split()
a, b = [int(a), int(b)]

print(f'{a} {b}', end=' ')
if b == 0:
  print('errados')
else:
  difer = b - a
  if difer == 1 or difer == 0:
      print('ok')
  else:
      print('errados')
