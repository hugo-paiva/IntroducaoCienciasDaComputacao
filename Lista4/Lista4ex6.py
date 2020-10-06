def mmc(x, y):
    if x == 1 and y == 1:
        return
    n = 1
    if x % n == 0:
        x = x/n
        print(x)
        return mmc(x/n, y)
    if y % n == 0:
        y = y/n
        print(y)
        return mmc(x, y/n)
    


a = b = 1
while a > 0 and b > 0:
    a, b = input().split()
    a, b = int(a), int(b)
    mmc(a, b)
