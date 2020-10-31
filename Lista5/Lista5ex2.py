frase = input()
for letra in frase:
    if letra not in 'AEIOUaeiou áéíóú':
        frase = frase.replace(letra, 'p')
print(frase)
