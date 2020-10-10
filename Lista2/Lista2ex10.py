tempo1, velocidade1, tempo2, velocidade2 = input().split()
tempo1, velocidade1, tempo2, velocidade2 = int(tempo1), int(velocidade1),  int(tempo2), int(velocidade2)

pontossemVelox = pontoscomVelox = pontosTotalSemVelox = pontosTotalComVelox = 0

for tempo_trecho, tempo, velocidade, limite, penalidade in [ [1800, tempo1, velocidade1, 60, 10], [3600, tempo2, velocidade2, 40, 20] ]:
  if tempo > tempo_trecho:
    pontossemVelox -= tempo - tempo_trecho
  else:
    pontossemVelox -= 2*(tempo_trecho - tempo)
  print(pontossemVelox)
  pontosTotalSemVelox += pontossemVelox
  #Velocidade
  if velocidade > limite:
    pontoscomVelox -= penalidade*(velocidade - limite)
  print(pontossemVelox + pontoscomVelox)
  pontosTotalComVelox += pontoscomVelox
  pontossemVelox = pontoscomVelox = 0

print(pontosTotalSemVelox)
print(pontosTotalComVelox + pontosTotalSemVelox)