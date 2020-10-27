codigo, quant_KWh = input().split()
somatorio_consumos = soma_media = cont_media = 0

while codigo != '0':
    codigo, quant_KWh = int(codigo), int(quant_KWh)
    if codigo == 1: # Residencial
        if quant_KWh <= 200:
            preco_consumo = quant_KWh * 0.60
        else:
            preco_consumo = quant_KWh * 0.85
        soma_media += quant_KWh
        cont_media += 1
    if codigo == 2: # Comercial
        if quant_KWh <= 800:
            preco_consumo = quant_KWh * 0.72
        else:
            preco_consumo = quant_KWh * 0.83
        soma_media += quant_KWh
        cont_media += 1
    if codigo == 3: # Industrial
        if quant_KWh <= 3000:
            preco_consumo = quant_KWh * 0.75
        else:
            preco_consumo = quant_KWh * 0.8
    somatorio_consumos += quant_KWh
    print(f'{preco_consumo:.2f}')

    codigo, quant_KWh = input().split()

print(somatorio_consumos, end=' ')
if soma_media > 0:
    print(f'{soma_media/cont_media:.0f}')
else:
    print(0)
