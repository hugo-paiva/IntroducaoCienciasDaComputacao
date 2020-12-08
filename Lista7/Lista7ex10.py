def converter_em_min(string):
    hora, minuto = [int(num) for num in string.split(':')]
    return minuto + hora * 60


atividades = {}

for _ in range(int(input())):
    *atividade, inicio, fim = input().split()
    atividades[' '.join(atividade)] = {'inicio': converter_em_min(inicio), 'fim': converter_em_min(fim)}

dia_perfeito = []
final = -1
for atividade in sorted(atividades, key=lambda atividad: atividades[atividad]['fim']):
    if atividades[atividade]['inicio'] < final:
        continue
    dia_perfeito.append(atividade)
    final = atividades[atividade]['fim']

print(len(dia_perfeito), *dia_perfeito, sep='\n')
