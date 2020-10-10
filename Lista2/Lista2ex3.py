cargo = input().lower().strip()
tempo = int(input())
salarioAtual = float(input())

if salarioAtual < 1039:
    print('Salário inválido!')
else:
    if cargo == 'gerente':
        if tempo <= 3:
            reajuste = salarioAtual * 0.12
        elif tempo <= 6:
            reajuste = salarioAtual * 0.13
        else:
            reajuste = salarioAtual * 0.15
    elif cargo == 'engenheiro':
        if tempo <= 3:
            reajuste = salarioAtual * 0.07
        elif tempo <= 6:
            reajuste = salarioAtual * 0.11
        else:
            reajuste = salarioAtual * 0.14
    else:
        reajuste = salarioAtual * 0.05
    #Trecho chamado apenas se salarioAtual >= 1039
    salarioReajustado = salarioAtual + reajuste
    print(f'{reajuste:.2f}')
    print(f'{salarioReajustado:.2f}')
  