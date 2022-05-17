# 7. Criar um programa para ler a distância (em Km) e o consumo de combustível (em litros) de um carro ao percorrer um trajeto qualquer. Após as leituras, calcular e mostrar o consumo médio (em Km/litro) do carro e um aviso seguinto a tabela abaixo:

#   Consumo Médio (Km/litro)	Aviso!
#   Abaixo de 8	                Venda o carro!!
#   Entre 8 e 14	            Econômico!!
#   Acima de 14             	Super econômico!!

dist = float(input('\nDistância(Km/h): '))
comb = float(input('Consumo de combustível(L): '))
cm = dist / comb
print(f'\nO consumo médio do veículo = {cm:.1f} Km/L')

print(f'\nAviso: ', end='')
if cm < 8:
    print('Venda o carro!!')
elif cm < 14:
    print('Econômico!!')
else:
    print('Super econômico!!')