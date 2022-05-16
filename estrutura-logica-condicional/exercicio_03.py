# 3. Criar um programa para ler 3 valores inteiros e, após as leituras, mostrar o menor e o maior valor digitado pelo usuário, seguindo as regras:
# Usar apenas if (NÃO pode usar else, nem elif).
# NÃO pode usar o operador lógico and.

v1 = int(input('\nInsira o valor 1: '))
v2 = int(input('Insira o valor 2: '))
v3 = int(input('Insira o valor 3: '))

menor = v1
if v2 < menor:
    menor = v2
if v3 < menor:
    menor = v3

maior = v1
if v2 > maior:
    maior = v2
if v3 > maior:
    maior = v3

print(f'\nO Maior número é {maior} e o menor número é o {menor}.')
