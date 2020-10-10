num = int(input())
tentativa = int(input())
while tentativa != num:
    if tentativa > num:
        print('O número correto é menor.')
    elif tentativa < num:
        print('O número correto é maior.')
    tentativa = int(input())
print('Parabéns! Você acertou.')