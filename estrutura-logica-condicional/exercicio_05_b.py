# Outra forma: "método Python" de trocar.
prim = float(input('\nPrimeiro Número: '))
seg = float(input('Segundo Número: '))

if prim > seg:
    prim, seg = seg, prim

print(f'\nO valor do primeiro númeero é {prim:.1f} e o do segundo é {seg:.1f}')