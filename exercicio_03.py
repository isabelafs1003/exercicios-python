# 3. Crie um programa para ler o preço de um produto e, após a leitura, calcular e mostrar o valor do produto após um desconto de 7% e o valor do produto após um aumento de 5,5%.

print("\nCalcule o Desconto e o Aumento de um Produto: ")

preco = float(input("\nValor do Produto: R$ "))

desc = preco - (preco * 7 / 100) # 7% de desconto
aum = preco + (preco * 5.5 / 100) # 5,5% de aumento

print(f"\nO Valor do Produto após o desconto de 7%: R$ {desc:.2f}")
print(f"\nO Valor do Produto após um aumento de 5,5%: R$ {aum:.2f}")
