# Criar um programa para ler a idade e o tempo de serviço de um trabalhador (em anos) e, após as leituras, mostrar uma mensagem informando se ele pode ou não se aposentar. As condições para aposentadoria são:

# Ter pelo menos 65 anos de idade.
# Ou ter trabalhado pelo menos 30 anos.
# Ou ter pelo menos 60 anos de idade e ter trabalhado pelo menos 25 anos.

idade = int(input('\nInforme sua idade: '))
tempo = int(input('Informe seu tempo de serviço: '))

if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
    print('\nPoderá se aposentar!')
else:
    print('\nNão poderá se aposentar!')