# 5. Uma empresa paga aos seus funcionários um salário fixo mais uma comissão de 7,5% sobre as vendas realizadas por cada funcionário. Sabendo disso, crie um programa para ler o salário fixo e o valor das vendas de um funcionário e, após a leitura, calcular e mostrar a comissão sobre as vendas e o salário final desse funcionário.

print("\nCalcule a comissão e o salário final dos funcionários: ")

sal_fix = float(input("\nInforme o Salário Fixo: R$ "))
vendas = float(input("Informe o Valor Total de Vendas: R$ "))

com = vendas * (7.5 / 100)
sal_fin = sal_fix + com

print(f"\nO valor Total das Comissões é: R$ {com:.2f}")
print(f"O Salário Final é: R$ {sal_fin:.2f}")