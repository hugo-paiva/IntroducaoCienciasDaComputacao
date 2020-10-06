'''num = int(input())
fatorial = 1
for termo in range(1, num + 1):
    fatorial *= termo
print(fatorial)'''

def fatorial(num):
    if num == 1:
        return 1
    return num * fatorial(num - 1)

print(fatorial(5))
