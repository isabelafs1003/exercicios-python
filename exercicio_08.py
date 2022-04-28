# 8. Crie um programa para ler uma certa quantidade de dias, horas, minutos e segundos (o usuário fornece). Após as leituras, calcular e mostrar a qtde total de segundos contidos nesses valores.

print("Converta Dias, Horas, Minutos e Segundos em Segundos:")

d = float(input("\nInsira os Dias: "))
ds = d * (24 * 60 * 60)

h = float(input("Insira as Horas: "))
hs = h * (60 * 60)

m = float(input("Insira os Minutos: "))
ms = m * 60

s = float(input("Insira os Segundos: "))

total = ds + hs + ms + s

print(f"\n{ds:.0f} + {hs:.0f} + {ms:.0f} + {s:.0f} = {total:.0f} Segundos.")