sequencia = input()

while sequencia != 'fim':
    erro = False
    for char in sequencia:
        if char not in '01':
            erro = True
            print('erro')
            break
        
    if erro == False:
        paridade = sequencia.count('1')
        if paridade % 2 == 0:
            print('0')
        else:
            print('1')

    sequencia = input()
