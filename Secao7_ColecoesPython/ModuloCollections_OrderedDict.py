"""
Um dicionário que garante a ordem dos elementos
"""

#  Import
from collections import OrderedDict
dicio = OrderedDict({'a': 1, 'b': 2})
for chave, valor in dicio.items():
    print(f'Chave{chave}:valor{valor}')

#  No dicionário comum, a ordem dos elementos não tem importancia
#  No dicionário OrderedDict, a ordem dos elementos tem importancia

