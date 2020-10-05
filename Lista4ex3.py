def eh_par(n):
    if n < 2:
        return ''
    if n % 2 != 0:
        n -= 1
    print(n)
    return eh_par(n-2)


x = int(input())
print(eh_par(x))
