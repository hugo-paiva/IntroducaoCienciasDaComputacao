num_trabalhos = int(input())
trabalho = {}
gaveta = []
for _ in range(num_trabalhos):
    trabalho['arquivo'], *trabalho['tags'] = input().split()
    gaveta.append(trabalho.copy())
busca = input().split()

for trabalho in gaveta:
    for item in busca:
        if item in trabalho['tags']:
            print(trabalho['arquivo'])
            break
