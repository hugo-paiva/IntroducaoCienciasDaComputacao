def header(frase, tam=72):
    print(linha())
    print(f'{frase.center(tam)}')
    print(linha())
    print('Criado por Hugo Paiva.'.rjust(tam))


def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados.\033[m')
            continue
        except:
            print('\033[31mERRO! Por favor digite um número inteiro válido.\033[m')
        else:
            return valor


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg).replace(',', '.'))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados.\033[m')
            continue
        except:
            print('\033[31mERRO! Por favor digite um número inteiro válido.\033[m')
            return 0
        else:
            return valor


def linha(tam=72):
    return '-' * tam


def menu(lista):
    header('O que deseja fazer?')
    cont = 1
    for linha in lista:
        print(f'[ {cont} ] {linha}')
        cont += 1
    return leiaInt('Digite um número válido: ')


def juros_compostos_aportes():
    header('Calculadora de Juros Compostos com Aportes Mensais')

    # Input de dados
    prazo = leiaInt('Digite o número de anos que deseja manter o dinheiro investido: ') * 12
    aportes_mensais = leiaFloat('Digite o valor dos aportes mensais: R$')
    taxa_juros = leiaFloat('Digite o valor do juros mensais: ')
     
    # Calculos referentes aos juros compostos com aportes
    montante = (aportes_mensais * (((100 + taxa_juros)/100)**prazo - 1)/ (taxa_juros/100))
    total_investido = aportes_mensais * prazo

    header('RESULTADOS')

    print(f'O valor R${aportes_mensais} investido mensalmente durante um prazo de {prazo} meses\
         \na uma taxa de {taxa_juros} ao mês gera o montante de R${montante:.2f}')

    lucro(total_investido, montante)


def juros_compostos():
    header('Calculadora de Juros Compostos')

    # Input de dados
    prazo = leiaInt('Digite o número de anos que deseja manter o dinheiro investido: ') * 12
    aporte_unico = leiaFloat('Qual o valor depositado: R$')
    taxa_juros = leiaFloat('Digite o valor do juros mensais: ')

    # Calculos referentes aos juros compostos
    montante = aporte_unico * ((100 + taxa_juros)/100)**prazo
    total_investido = aporte_unico

    header('RESULTADOS')

    print(f'O valor inicial único de R${aporte_unico} investido durante um prazo de {prazo} meses\
         \na uma taxa de {taxa_juros} ao mês gera o montante de R${montante:.2f}')
    
    lucro(total_investido, montante)


def lucro(total_investido, montante):
    print(f'\nTotal investido: R${total_investido:.>25.2f}')
    print(f'Lucro em reais: R${montante-total_investido:.>26.2f}')
    print(f'Lucro percentual total: {(montante-total_investido)/(total_investido)*100:.>20.2f} %')


def juros_entrada_n_aportes():
    header('Calculadora de Investimento Com Entrada e Aportes Mensais')

    # Input de dados
    prazo = leiaInt('Digite o número de anos que deseja manter o dinheiro investido: ') * 12
    aporte_unico = leiaFloat('Qual o valor depositado: R$')
    aportes_mensais = leiaFloat('Digite o valor dos aportes mensais: R$')
    taxa_juros = leiaFloat('Digite o valor do juros mensais: ')
    
    # Calculos referentes aos juros compostos com aportes
    montante1 = (aportes_mensais * (((100 + taxa_juros)/100)**prazo - 1)/ (taxa_juros/100))
    total_investido1 = aportes_mensais * prazo

    # Calculos referentes aos juros compostos
    montante2 = aporte_unico * ((100 + taxa_juros)/100)**prazo
    total_investido2 = aporte_unico

    header('RESULTADOS')

    print(f'O valor R${aportes_mensais} investido mensalmente durante um prazo de {prazo} meses\
         \na uma taxa de {taxa_juros} ao mês gera o montante de R${montante1:.2f}')

    print(f'O valor inicial único de R${aporte_unico} investido durante um prazo de {prazo} meses\
         \na uma taxa de {taxa_juros} ao mês gera o montante de R${montante2:.2f}')

    # Somatório do orçamento
    header('Somatório do orçamento')
    print(f'Montante final: R${montante1+montante2:.>26.2f}')
    lucro(total_investido1 + total_investido2, montante1 + montante2)
        

from time import sleep

quer_continuar = 's'
while quer_continuar in 's':
    
    while True:
        opcao = menu(['Calcular rendimento de investimento com Aportes Mensais', 'Calcular rendimento de um único aporte', 'Calcular rendimento com entrada + aportes'])
        if opcao in [1, 2, 3]:
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
            sleep(2)

    if opcao == 1: juros_compostos_aportes()
    if opcao == 2: juros_compostos()
    if opcao == 3: juros_entrada_n_aportes()

    quer_continuar = input('\nQuer fazer outro cálculo? [s/n]').strip().lower()

print('Até mais! Volte sempre que precisar!')
