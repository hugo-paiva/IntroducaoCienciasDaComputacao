backup = {}

def acker(x,y):
    if (x,y) in backup:
        return backup[x,y]
    if x == 0:
        backup[x,y] = y + 1
    elif x == 1:
        backup[x,y] = y + 2
    elif x == 2:
        backup[x,y] = 2*y + 3
    elif x == 3:
        backup[x,y] = 2**(y+3)-3
    elif y == 0:
        backup[x,y] = acker(x-1, 1)
    else:
        backup[x,y] = acker(x-1, acker(x,y-1))
    return backup[x,y]


a, b = input().split()
a, b = int(a), int(b)
print(acker(a, b))