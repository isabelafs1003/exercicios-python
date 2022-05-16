# 7. Uma escada está apoiada no chão formando um ângulo a e há uma distância d da parede. A parede forma um ângulo de 90º com o chão. Sabendo disso, crie um programa para ler os valores de a (graus) e d (metros), calcule e mostre o comprimento da escada (c).
# |\
# | \
# |  \
# |   \                      d
# |    \ c         cos a = -----  ->  c = d / cos a
# |     \                    c
# |      \
# |_      \
# |.|    a \
# -----------
#      d


from math import cos, radians
print("\nCálculo do Comprimento da Escada: ")

a = float(input("\nÂngulo (graus): "))
d = float(input("Distância (metros): "))

c = d / cos(radians(a))

print(f"\nO comprimento da escada é: {c:.1f} m")