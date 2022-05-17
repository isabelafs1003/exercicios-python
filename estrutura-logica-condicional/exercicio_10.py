# 10. Criar um programa para ler 3 valores reais (float) e, após as leituras, verificar se os valores podem ou não formar um triângulo. Caso formem um triângulo, mostrar qual o seu tipo.

# Regra para formar um triângulo: cada um dos lados deve ser menor que a soma dos outros dois lados.
# Tipos: equilátero (3 lados iguais), isósceles (apenas 2 lados iguais) ou escaleno (3 lados diferentes).

a = float(input('\nInsira o valor 1: '))
b = float(input('Insira o valor 2: '))
c = float(input('Insira o valor 3: '))

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print('\nTriângulo Equilátero!')
    elif a == b or b == c or a == c:
        print('\nTriângulo Isósceles!')
    else:
        print('\nTriângulo Escaleno!')
else:
    print('\nNão formam um Triângulo!')
