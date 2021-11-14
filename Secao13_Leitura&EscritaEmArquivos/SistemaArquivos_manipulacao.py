"""

import os

#  Verificando se o arquivo existe ou não

print(os.path.exists("cursoPy"))  # Retorna True ou False
print(os.getcwd())

#  Criando arquivo localmente

# Exemplo1 - Forma não aconselhavel
open('arquivo.txt', 'w').close()


#  Exemplo2 - Forma aconselhável
with open('arquivo2.txt', 'w') as arq:
    pass  # = não faça nada 


"""

import os




