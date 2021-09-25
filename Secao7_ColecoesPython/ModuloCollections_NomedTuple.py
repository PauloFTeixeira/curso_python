"""
São tuplas, diferenciadas, onde especificamos um nome para a mesma e também parâmetros

Coloca-se variáveis dentro da tupla, algo parecido com dict
"""

#  Import
from collections import namedtuple

#  DEFINIÇÃO DE NOMES E PARÂMETROS
#  Forma 1 de Declaração
racao = namedtuple('racao', 'preco tipo indicação')

#  Forma 2 de Declaração
racao2 = namedtuple('racao', 'preco, tipo, indicação')

#  Forma 3 de Declaração
racao3 = namedtuple('racao', ['preco', 'tipo', 'indicação'])

#  USANDO
r1 = racao3(preco=68, tipo='farelada', indicação='gado geral')
touro = racao3(preco=69, tipo='farelada', indicação='gado geral em campo nativo')
print(r1)

#  ACESSANDO OS DADOS
#  Forma 1
print(r1[0])
print(r1[1])
print(r1[2])

#  Forma 2
print(touro.preco)
print(touro.tipo)
print(touro.indicação)
