# 6. Crie um programa para ler os valores dos catetos de um triângulo retângulo e, após a leitura, calcular e mostrar o valor da hipotenusa.
# Obs.: use Pitágoras para calcular.
# h= V(ca²+cb²)

from math import sqrt
print("\nCalcule o Valor da Hipotenusa: ")

ca = float(input("\nValor do Cateto 1: "))
cb = float(input("Valor do Cateto 2: "))

h = sqrt(ca ** 2 + cb ** 2)

print(f"\nO valor da Hipotenusa é: {h:.2f}")