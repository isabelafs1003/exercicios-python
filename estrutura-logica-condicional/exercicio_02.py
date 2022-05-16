# 2. Criar um programa para ler 3 valores inteiros e, após as leituras, mostrar o menor e o maior valor entre os 3.

v1 = float(input('\nInsira o valor 1: '))
v2 = float(input('Insira o valor 2: '))
v3 = float(input('Insira o valor 3: '))

# maior
if v1 > v2 and v1 > v3:
    print(f'\nO valor 1 é o MAIOR = {v1:.1f}')
elif v2 > v3 and v2 > v1:
    print(f'\nO valor 2 é o MAIOR = {v2:.1f}')
else:
    print(f'\nO valor 3 é o MAIOR = {v3:.1f}')

# menor
if v1 < v2 and v1 < v3:
    print(f'O valor 1 é MENOR = {v1:.1f}')
elif v2 < v1 and v2 < v3:
    print(f'O valor 2 é MENOR: {v2:.1f}')
else:
    print(f'O valor 3 é o MENOR = {v3:.1f}')