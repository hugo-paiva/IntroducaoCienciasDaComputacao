horai, mini, horaf, minf = input().split()
horai, mini, horaf, minf = int(horai), int(mini), int(horaf), int(minf)

if horaf <= horai and minf < mini:
  reshora = 24 - horai + horaf - 1
  resmin = 60 - mini + minf
elif horaf <= horai and minf >= mini:
  reshora = 24 - horai + horaf
  resmin = minf - mini
elif horaf > horai and minf < mini:
  reshora = horaf - horai - 1
  resmin = 60 - mini + minf
elif horaf > horai and minf > mini:
  reshora = horaf - horai
  resmin = minf - mini

print(f'O jogo durou {reshora} hora(s) e {resmin} minuto(s).')
