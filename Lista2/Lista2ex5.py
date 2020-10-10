a = str(input())
b = str(input())

sizeA = len(a)
sizeB = len(b)

if a == b:
  print('-1')
else:
  if len(a) > len(b):
    print(len(a))
  else:
    print(len(b))
