"""Forca"""
resposta = "banana"
vidas = min(5,len(resposta))

input("""
Bem vindo à forca
Pressione Enter para começar""")
preview = '_'*len(resposta)
print(preview)
while vidas > 0:
    chute = input()[:1]
    # chute está dentro da resposta?
    if chute in resposta:
        preview = ''.join([l_res if l_pre == '_' and chute == l_res else l_pre\
                           for l_res,l_pre in zip(list(resposta),list(preview))])
        """
        percorrer a resposta comparando letra a letra com preview
            se letra no preview == '_':
               se chute == letra na resposta:
                   preview += letra da resposta
            caso contrário:
               preview += letra do preview                
        """
    else:
        vidas -= 1
        print(f'errou, {vidas} vidas restantes')
    print(preview)
    if '_' not in preview:
        break
print('endgame')
