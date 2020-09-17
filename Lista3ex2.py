t = int(input())
for c in range(2):
    a, b = input().split()
    a, b = [int(a), int(b)]
    for c in range(a, a + b +1):
      cont += 1
      print(c, end=' ' if cont == b else end='')