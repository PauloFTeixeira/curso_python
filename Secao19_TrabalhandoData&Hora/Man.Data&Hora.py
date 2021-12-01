"""
Módulo integrado para trabalhar com data e hora chamado datetime




print(dir(datetime))
print(datetime.MAXYEAR)  # Máximo ano suportado
print(datetime.MINYEAR)  # Mínimo ano suportado

#  Dentro do modulo datetime, na classe datetima, o atributo now()
print(datetime.datetime.now())  # Retorna date e hora corrente

#  Para fazer ajustes na data/hora

inicio = datetime.datetime.now()
print(inicio)
# Para alterar
inicio = inicio.replace(hour=12, minute=0, second=0, microsecond=0)
print(inicio)






#  RECEBENDO DATAS DO USUÁRIO

evento = datetime.datetime(2020, 1, 1, 0)  # 1/1/2022 às 00:00
print(evento)

nascimento = input('Informa sua data de nascimento (dd/mm/aaaa): ')
print(nascimento)
print(type(nascimento))
#  Transformar a string em Data
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))
"""

import datetime

#  ACESSANDO INDIVIDUAL DOS ELEMENTOS

datahora = datetime.datetime.now()
print(datahora.year)
print(datahora.month)
print(datahora.day)
print(datahora.hour)
print(datahora.minute)
print(datahora.second)
print(datahora.microsecond)




