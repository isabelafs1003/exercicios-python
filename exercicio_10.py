# 10. Crie um programa para ler uma qtde qualquer de segundos e converter para dias, horas, minutos e segundos restantes.

# Ler Segundos e converter para dias, horas, minutos e segundos

seg = int(input('Por favor, insira a quantidade desejada de segundos para conversão: '))

# se coloca duas barras pois assim não dá o resultado em decimal.

min = seg // 60
seg %= 60           # seg = seg % 60 --> a % serve para calcular o resto  
hr = min // 60
min %= 60
dia = hr // 24
hr %= 24


print(f'\nRestam {dia} dias, {hr} horas, {min} minutos e {seg} segundos.')