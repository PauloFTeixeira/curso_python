"""
Usado para salvar dados em .csv de forma mais segura

A sua função:
Objeto Python -> Binarização
Binarização -> Objeto Python

Processo chamado serialização/deserialização

OBS.: Não é seguro contra dados maliciosos, não trabalhar com arquivos de fontes não seguras

"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome
    
    def comer(self):
        print(f'{self.__nome} está comendo...')
    
class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} está miando...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self._Animal__nome} está latindo...')
    

felix = Gato('Felix')
pluto = Cachorro('Pluto')


#  Criando o arquivo Pickle (Escrevendo)
with open('animais.pickle', 'wb') as arq:
    pickle.dump((felix, pluto), arq)


#  Fazendo a Leitura do arquivo
with open('animais.pickle', 'rb') as arq:
    gato, cachorro = pickle.load(arq)
    print(f'O gato chama-se {gato._Animal__nome}')
    gato.mia()
    print(f'O tipo de gato é {type(gato)}')
    print()
    print(f'O cachorro chama-se {cachorro._Animal__nome}')
    cachorro.late()
    print(f'O tipo de cachorro é {type(cachorro)}')


