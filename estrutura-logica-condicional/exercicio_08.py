# 8. Criar um programa para ler a idade (em anos) de um nadador e, após a leitura, mostrar sua categoria seguindo a tabela abaixo:
#   Categoria	        Idade (em anos)
#   NA	                Abaixo de 5
#   Infantil A	        5 a 7
#   Infantil B	        8 a 10
#   Juvenil A	        11 a 14
#   Juvenil B	        15 a 18
#   Senior	            Acima de 18

idade = int(input('\nQuantos anos você tem? '))

if idade < 5:
    cat = 'NA'
elif idade <= 7:
    cat = 'Infantil A'
elif idade <= 10:
    cat = 'Infantil B'
elif idade <= 14:
    cat = 'Juvenil A'
elif idade <= 18:
    cat = 'Juvenil B'
else: 
    cat = 'Senior'

print(f'\nCategoria: {cat}')
