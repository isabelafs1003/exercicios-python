# 5. Criar um programa para ler 2 valores reais (float) e, caso o primeiro valor seja maior que o segundo, trocar os valores das duas variáveis e mostrar seus resultados.

prim = float(input('\nPrimeiro Número: '))
seg = float(input('Segundo Número: '))

if prim > seg:
    aux = prim
    prim = seg
    seg = aux

print(f'\nO primeiro número é {prim:.1f} e o segundo número é {seg:.1f}')