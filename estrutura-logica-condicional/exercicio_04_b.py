# Observação: o operador % pode ser usado para verificar se um número é múltiplo de qualquer outro número.
print('\nVerifique se um número é múltiplo de outro')
x = int(input('\nDigite um número:'))
y = int(input('\nDigite outro número:'))

if x % y == 0:
    print(f'\n{x} é múltiplo de {y}')
else:
    print(f'\n{x} não é múltiplo de {y}')

