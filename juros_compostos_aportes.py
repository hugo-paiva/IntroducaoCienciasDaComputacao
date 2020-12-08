def titulo(frase):
    print(f'{frase:-^72}')

def corrigir_sep_decimal(tupla):
    for idx,num in enumerate(tupla):
        if ',' in num:
            tupla[idx] = num.replace(',','.')
    return tupla


def juros_compostos_aportes():
    titulo(' Calculadora de Juros Compostos com Aportes Mensais ')

    print('Criado por Hugo Paiva.'.rjust(72))
    '''prazo = int(input('Digite o número de meses que deseja manter o dinheiro investido: '))
    aportes_mensais = (float(input('Digite o valor dos aportes mensais: R$')))
    taxa_juros = float(input('Digite o valor do juros mensais usando ponto como separador decimal: '))'''
    prazo, aportes_mensais, taxa_juros = corrigir_sep_decimal(input('''Informe separando com espaços:
    Quantos anos deseja manter o dinheiro investido? Informe valor dos 
    aportes e juros mensais: '''
        ).split())
    prazo, aportes_mensais, taxa_juros = int(prazo)*12, float(aportes_mensais), float(taxa_juros)

    montante = (aportes_mensais * (((100 + taxa_juros)/100)**prazo - 1)/ (taxa_juros/100))

    titulo(' RESULTADOS ')

    print(f'O valor R${aportes_mensais} investido mensalmente durante um prazo de {prazo} meses\
         \na uma taxa de {taxa_juros} ao mês gera o montante de R${montante:.2f}')
    print(f'Lucro em reais: R${montante-aportes_mensais*prazo:.2f}')
    print(f'Lucro percentual: {(montante-aportes_mensais*prazo)/(aportes_mensais*prazo)*100:.2f}%')


def juros_compostos():
    titulo(' Calculadora de Juros Compostos ')

    print('Criado por Hugo Paiva.'.rjust(72))
    prazo, aportes_mensais, taxa_juros = corrigir_sep_decimal(input('''Informe separando com espaços:
    Quantos anos deseja manter o dinheiro investido? Qual o valor depositado e juros mensais: ''').split())
    prazo, aportes_mensais, taxa_juros = int(prazo)*12, float(aportes_mensais), float(taxa_juros)

    montante = aportes_mensais * ((100 + taxa_juros)/100)**prazo

    titulo(' RESULTADOS ')

    print(f'O valor inicial R${aportes_mensais} investido durante um prazo de {prazo} meses\
         \na uma taxa de {taxa_juros} ao mês gera o montante de R${montante:.2f}')
    print(f'Lucro em reais: R${montante-aportes_mensais:=>20.2f}')
    print(f'Lucro percentual: {(montante-aportes_mensais)/(montante)*100:=>20.2f}%')


opcao = 0
quer_continuar = 's'
while 's' in quer_continuar:
    print('Seja bem vindo!')
    print('-'*72)

    while True:
        opcao = int(input('''O que deseja fazer?
    [ 1 ] Calcular rendimento de investimento com Aportes Mensais
    [ 2 ] Calcular rendimento de um único aporte
    Digite um número válido: '''))
        if opcao in [1,2]:
            break
    if opcao == 1: juros_compostos_aportes()
    if opcao == 2: juros_compostos()

    quer_continuar = input('\nQuer fazer outro cálculo? [s/n]').strip().lower()

print('Até mais! Volte sempre que precisar!')
