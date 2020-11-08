snake_case = input().split('_')
CamelCase = ''
for index, palavra in enumerate(snake_case):
    snake_case[index] = palavra.capitalize()
print(CamelCase.join(snake_case))