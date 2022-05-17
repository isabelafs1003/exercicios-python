# Criar um programa para ler uma data (dia, mês e ano) e, após a leitura, mostrar uma mensagem informando se a data é válida ou inválida.

# Dica:
# d, m, a = input('Data (dd/mm/aaaa): ').split('/') --> split = dividir o conteúdo da variável de acordo com as condições especificadas em cada parâmetro da função ou com os valores predefinidos por padrão.

d, m, a = input('Data (dd/mm/aaaa): ').split('/')
d, m, a = int(d), int(m), int(a)

val = True # val é a variável que indica se a data é válida ou não (flag)

if a < 1 or m < 1 or m > 12 or d < 1 or d > 31:
    val = False
elif (m == 4 or m == 6 or m == 9 or m == 11) and d > 30:
    val = False
elif m == 2:
    if a % 4 == 0: # ano bissexto (múltiplo de 4)
        if d > 29:
            val = False
    elif d > 28: # ano não bissexto
        val = False

if val:
    print('\nVÁLIDA!!!')
else:
    print('\nINVÁLIDA!!!')