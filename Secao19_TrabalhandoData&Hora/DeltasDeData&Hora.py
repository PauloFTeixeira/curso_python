"""
Calculo de Datas

Delta é a diferença entre duas datas
Ex.: Data final - Data incial

"""

import datetime

hoje = datetime.datetime.now()
niver = datetime.datetime(2021, 12, 19, 0)

tempo = niver - hoje

print(type(tempo))
print(repr(tempo))

#  Uma data subtraida de outra, gera um timedelta
