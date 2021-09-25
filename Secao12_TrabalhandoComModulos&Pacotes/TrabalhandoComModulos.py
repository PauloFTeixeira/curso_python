"""
Módulos são outros arquivos em python
Módulos Random -> possui a função para geração de npumeros pseudoaleatórios


-------------------------------------------------------------------------------------------------------------------
  Importando todos os módulos - Não recomendado
import random
num = random.random()

#  Desta forma, todas as funções, classes e métodos foram armazenados em memória
#  Usando o DIR pode-se ver todas as propriedades para ver o que pode ser usado.
#  Para saber como usar determinada função, usa-se "help(random.random)"
print(help(random.normalvariate))

#  Para entrar no código fonte de uma função - segure <ctrl + click na função>

-------------------------------------------------------------------------------------------------------------------
#  Importando uma função específica de um módulo
#  from = do
from random import random  # numero entre 0 e 1
from random import uniform  # numero entre valores estabelecidos
from random import randint  # numero inteiro entre valores estabelecidos
from random import choice  # Escolhe um valor dentre um iterável
from random import shuffle  # Embaralha os dados de um iterável

-------------------------------------------------------------------------------------------------------------------

"""




