# Criar um programa para ler um número inteiro qualquer e, após a leitura, mostrar se o número é PAR ou ÍMPAR.

num = int(input('\nDigite um número inteiro: '))

if num % 2 == 0:
    print(f'\n{num} é PAR!')
else:
    print(f'\n{num} é ÍMPAR!')
