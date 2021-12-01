"""
JSON - JavaScript Object Notation
API - São meios de cominicação entre os serviços oferecidos por empresas e terceiros

import json

# JSON não trbalha com aspas simples '', dumps faz a formatação para aspas duplas ""
ret = json.dumps(['produto', {'Play': ('2TB', 'Novo', '220V', '2340')}])

print(type(ret))
print(ret)




import json

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    

gato = Gato('Tom', 'Vira-lata')
print(gato.__dict__)
print()
ret = json.dumps(gato.__dict__)
print(ret)
#  Arquivos JSON nada mais são que dicinários

"""

#  Integrando JSON com PICKLE
#  pip install jsonpickle


# NÃO FUNCIONOU

# Para encriptar
# import jsonpickle
# 
# class Gato:
# 
#     def __init__(self, nome, raca):
#         self.__nome = nome
#         self.__raca = raca
#     
#     @property
#     def nome(self):
#         return self.__nome
#     
#     @property
#     def raca(self):
#         return self.__raca
#     
# 
# gato = Gato('Tom', 'Vira-lata')
# 
# ret = jsonpickle.encode(gato)
# print(ret)

# Para ler o arquivo Json

with open('felix.json', 'r') as arq:
    conteudo = arq.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))

"""Após abrir o arquivo json, ele já desolve o objeto python, pronto para ser trabalhado"""
