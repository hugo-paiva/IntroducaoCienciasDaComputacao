alunos = int(input())
cont_aprovados = soma_geral = 0
for aluno in range(alunos):
    a, b, c, faltas = input().split()
    a, b, c, faltas = [float(a), float(b), float(c), int(faltas)]
    media = (a + b + c)/ 3
    print(f'{media:.1f}', end=' ')
    if media >= 5 and faltas <= 16:
        print('Aprovado')
        cont_aprovados += 1
    elif media >= 3 and faltas <= 16:
        print('Exame')
    else:
        print('Reprovado')
    soma_geral += media
media_turma = soma_geral / alunos
print(f'{media_turma:.1f} {cont_aprovados}')