# Criar um programa para ler 2 valores reais (float) e, após as leituras, mostrar o menu de opções mostrado abaixo e ler a escolha do usuário. Após a escolha, calcular e mostrar o resultado da operação selecionada. Caso a opção escolhida seja inválida, mostrar uma mensagem ao usuário.

# Exemplo de execução:
# Opções:
# 1. Soma dos dois valores.
# 2. Diferença dos dois valores (maior - menor).
# 3. Multiplicação dos dois valores.
# 4. Divisão dos dois valores (1º pelo 2º).
# Escolha:

# from IPython.display import clear_output

v1 = float(input('Valor 1: '))
v2 = float(input('\nValor 2: '))
# clear_output(True) # limpa a saída de dados
print('Opções:')
print('1 - Soma dos dois valores.')
print('2 - Diferença dos dois valores (maior - menor).')
print('3 - Multiplicação dos dois valores.')
print('4 - Divisão dos dois valores (1º pelo 2º).')
op = int(input('Escolha: '))

if op == 1:
    soma = v1 + v2
    print(f'\nSoma = {v1} + {v2} = {soma}')
elif op == 2:
    if v1 < v2:
        v1, v2 = v2, v1 # troca o valor de v1 com v2, se v1 for menor que v2
    dif = v1 - v2
    print(f'\nDiferença = {v1} - {v2} = {dif}')
elif op == 3:
    mult = v1 * v2
    print(f'\nMultiplicação = {v1} * {v2} = {mult}')
elif op == 4:
    div = v1 / v2
    print(f'\nDivisão = {v1} / {v2} = {div}')
else:
    print(f'\nOpção inválida!!')