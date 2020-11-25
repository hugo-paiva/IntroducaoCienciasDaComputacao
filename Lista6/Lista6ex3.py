quant_fatias, premiada = input().split()
quant_fatias, premiada = int(quant_fatias), int(premiada)

ganhador = ''
bolo_fatiado = list(range(quant_fatias))
for _ in range(quant_fatias):
    cliente, pedido = input().split()
    pedido = int(pedido)
    if bolo_fatiado[pedido] == premiada:
        ganhador = cliente
    del bolo_fatiado[pedido]
print(ganhador)
