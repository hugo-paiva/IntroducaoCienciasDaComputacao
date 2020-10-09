def mmc(x, y):
    if a == 0 or b == 0:
        return 0
    return a * b // mdc(a, b)


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


a, b = input().split()
a, b = int(a), int(b)

while a >= 0 and b >= 0:
    print(mmc(a, b))

    a, b = input().split()
    a, b = int(a), int(b)
