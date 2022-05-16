# 2. Crie um programa para ler o raio (m) de um círculo e, após a leitura, calcular e mostrar:
# comp = 2 . PI . raio
# area = PI . raio²
# OBS.: PI = 3.1415

from math import pi
print("\nCalcule a Área e o Comprimento do Círculo:")

raio = float(input("\n Insira o Valor do Raio:"))

comp = 2 * pi * raio
area = pi * raio ** 2

print(f"\nO valor do Comprimento do Círculo é: {comp:.1f}")
print(f"\nO valor da Área do Círculo é: {area:.1f}")