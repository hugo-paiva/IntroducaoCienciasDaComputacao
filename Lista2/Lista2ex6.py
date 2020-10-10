mes, dia = input().split()
mes, dia = int(mes), int(dia)

ano = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
quantDiasMes = ano[mes - 1]

semana1 = 7 - dia + 1 #Contagem quantidade de dias da semana 1. Ex: Semana tem o primeiro dia no 7º dia da semana. 7 - 7 + 1 = 1 dia presente nesta semana
quantDiasMes = quantDiasMes - semana1
colunas = quantDiasMes//7 + 1     #Contagem das semanas completas centrais + 1ª semana
if quantDiasMes % 7 != 0:
  colunas += 1                    #Adição da semana incompelta final se existir

print(colunas)
