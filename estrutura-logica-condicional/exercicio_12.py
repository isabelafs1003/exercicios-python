# Criar um programa para ler a altura (m) e o peso (Kg) de uma pessoa e, após as leituras, mostrar a classificação dessa pessoa através da tabela abaixo:
#   Altura		        Peso	
#                   Até 60	  Entre 60 e 90 (inclusive)	  Acima de 90
#   Abaixo de 1,2	   A	            D	                    G
#   De 1,2 a 1,7	   B	            E	                    H
#   Acima de 1,7	   C	            F	                    I

alt = float(input('\nSua Altura(m): '))
peso = float(input('Seu Peso(Kg):'))

if alt < 1.2:
    if peso <= 60:
        cla = 'A'
    elif peso <= 90:
        cla = 'D'
    else:
        cla = 'G'
elif alt <= 1.7:
    if peso <= 60:
        cla = 'B'
    elif peso <= 90:
        cla = 'E'
    else:
        cla = 'H'
else:
    if peso <= 60:
        cla = 'C'
    elif peso <= 90:
        cla = 'F'
    else:
        cla = 'I'

print(f'\nClassificação: {cla}')