def eh_par_menos_dois(n):
    if n == 0:
        return 0
    elif n < 0:
        return -1
    if n % 2 != 0:
        n -= 1
    return n - 2 + eh_par_menos_dois(n - 2) 


print(eh_par_menos_dois(int(input())))
