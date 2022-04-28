# 1. Crie um programa para ler 3 notas (0 a 10) e, após a leitura, calcular e mostrar a média aritmética das notas.

print("\nMédia Aritmética:")

n1 = float(input("\nNota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
ma = (n1 + n2 + n3) / 3

print(f"\nA média Ritmética deste Aluno é: {ma:.1f}")