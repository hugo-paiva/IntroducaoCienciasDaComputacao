def maior():
    for c in range(10):
       num = int(input())
       if c == 0:
           maior = primeiro = num
       if num > maior:
           maior = num
    print(maior)
    if maior % primeiro == 0:
        print(primeiro)

maior()

