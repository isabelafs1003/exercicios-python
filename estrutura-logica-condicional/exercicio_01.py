# 1. Criar um programa para ler 2 notas, calcular e mostrar a média aritmética e informar se o aluno foi aprovado ou reprovado (média mínima = 6.0). Mostrar também uma mensagem de 'Parabéns!', caso ele tenha uma média igual a 10.

n1 = float(input('\nNota 1 (0 a 10): '))
n2 = float(input('Nota 2 (0 a 10): '))
ma = (n1 + n2) / 2
print(f'\nMédia final = {ma:.1f}')

if ma >= 6:
    print('\nAPROVADO!!!', end='') # end='' impede que o print vá para a próxima linha
    if ma == 10:
        print('  PARABÉNS!!!')
else:
    print('\nREPROVADO!!!')