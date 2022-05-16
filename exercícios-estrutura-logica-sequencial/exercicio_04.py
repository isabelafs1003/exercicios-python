# 4. Crie um programa para calcular e mostrar a média ponderada entre 2 notas. As notas e seus respectivos pesos devem ser fornecidos pelo usuário no início do programa.
# Fórmula:  mp= (n1.p1+n2.p2) / (p1+p2)

print("\nInsira dois valores para determinar a Média Ponderada entre as notas: ")

p1 = float(input("\nQual o peso da Nota 1: "))
n1 = float(input("Qual sua Nota 1: "))
p2 = float(input("\nQual o peso da Nota 2: "))
n2 = float(input("Qual sua Nota 2: "))

mp = (n1 * p1 + n2 * p2) / (p1 + p2)

print(f"\nA Média Ponderadas das Notas é: {mp:.2f}")