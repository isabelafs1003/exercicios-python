# Outra forma: fazer o mesmo que foi pedido no exercício 9 usando apenas 3 if's (sem else ou elif).

a = int(input('\nValor 1: '))
b = int(input('Valor 2: '))
c = int(input('Valor 3: '))

ca, cb, cc = a, b, c #copia das variaveis

if ca > cb:
    ca, cb = cb, ca

if cb > cc:
    cb, cc = cb, cc

if ca > cb:
    ca, cb = cb, ca

print(f'\n Ordem crescente: {ca}, {cb}, {cc}')