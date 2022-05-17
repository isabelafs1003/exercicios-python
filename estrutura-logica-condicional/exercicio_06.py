# 6. Criar um programa para ler 5 valores inteiros e, após as leituras, calcular e mostrar a qtde de valores negativos entre os 5 valores.
# Dica: use um contador.

v1 = int(input('\nPrimeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
v4 = int(input('Quarto valor: '))
v5 = int(input('Quinto valor: '))

qn = 0

if v1 < 0:
    qn += 1
if v2 < 0:
    qn += 1
if v3 < 0:
    qn += 1
if v4 < 0:
    qn += 1
if v5 < 0:
    qn += 1

print(f'\nQuantidade de números negativos = {qn}')