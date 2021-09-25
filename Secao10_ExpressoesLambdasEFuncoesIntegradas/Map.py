"""
Map

Com MAP se faz mapeamento de valores para funções.
É como se o 'map' fizesse um loop for em um iterável


-----------------------------------------------------------------------------------------------------------------

# EXEMPLO:                             NORMAL
#  Calcule a área de um círculo

import math
# r = raio

def area(r):
    return math.pi * (r ** 2)


print(area(4))
#  COM VÁRIOS DADOS
raios = [2, 3, 4, 5.25, 4.35]

#                                      FORMA 1
areas = []
for r in raios:
    areas.append(area(r))
print(areas)


#                                      FORMA 2
areas = map(area, raios)
print(areas)
print(type(areas))
#  gera um objeto tipo MAP

#  Os map sempre recebem dois parâmetros < função, iterável >

#                                      FORMA 3 - USANDO LAMBDA
print(list(map(lambda r : math.pi * (r ** 2), raios)))

#  OBS.:  Após usar os resultados da função map um vez, eles zeram!

-----------------------------------------------------------------------------------------------------------------
#  OUTRO EXEMPLO
cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19)]
#  Transformar ºC em ºF

v_para_f = lambda dado: (dado[0], (9 / 5) * dado [1] + 32)

print(list(map(v_para_f, cidades)))

"""







