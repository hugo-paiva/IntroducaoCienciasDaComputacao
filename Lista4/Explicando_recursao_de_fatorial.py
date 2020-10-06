# O código abaixo trata-se apenas de um exercício de imaginação, não sendo executável

def fatorial(num):
    if num == 1:
        return 1
    return 5 * fatorial(5 - 1) # num = 4 agora
                if 4 == 1:
                    return 1
                return 4 * fatorial(4 - 1) # num = 3 agora
                            if 3 == 1:
                                return 1
                            return 3 * fatorial(3 - 1) # num = 2 agora
                                        if 2 == 1:
                                            return 1
                                        return 2 * fatorial(2 - 1) # num = 1 agora
                                                    if 1 == 1:
                                                        return 1

    # Logo temos que:
    fatorial(5) = 5*fatorial(4)= 5 * 4 * fatorial(3)= 5 * 4 * 3 * fatorial(2) = 5 * 4 * 3 * 2 * fatorial(1)
    # Fatorial de 1 é 1
    # Portanto fatorial(5) = 5*4*3*2*1 = 120
