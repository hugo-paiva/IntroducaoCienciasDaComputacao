t = int(input())
for c in range(t):
    a, b = input().split()
    a, b = [int(a), int(b)]
    soma = cont = 0
    for c in range(a, a + b):
      soma += c
      cont += 1
      if cont < b:
        print(c, end=' ')
      else:
        print(c, end='\n')
    print(soma)