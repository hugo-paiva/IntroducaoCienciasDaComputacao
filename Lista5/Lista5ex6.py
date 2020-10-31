letras_sopa = input().lower()
letras_deixadas = input().lower()
cont_comida = cont_deixadas = 0
for letra in letras_sopa:
    if letra not in letras_deixadas and letra in 'john': # Significa que foi comida
        cont_comida += 1
    if letra in letras_deixadas and letra in 'john':
        cont_deixadas += 1
print(f'{cont_comida} {cont_deixadas}')
