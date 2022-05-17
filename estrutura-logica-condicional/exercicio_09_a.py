# 9. Criar um programa para ler 3 valores inteiros e, após as leituras, mostrá-los em ordem crescente.

a = int(input('\nValor 1: '))
b = int(input('Valor 2: '))
c = int(input('Valor 3: '))

print('\nOrdem crescente ', end='')
if a < b and b < c:
    print (f'{a}, {b}, {c}')
if a < c and c < b:
    print (f'{a}, {c}, {b}')
if b < a and a < c:
    print (f'{b}, {a}, {c}')
if b < c and c < a:
    print (f'{b}, {c}, {a}')
if c < a and a < b:
    print (f'{c}, {a}, {b}')
else:
    print (f'{c}, {b}, {a}')