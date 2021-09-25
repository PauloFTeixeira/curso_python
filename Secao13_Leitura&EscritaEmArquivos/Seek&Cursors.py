"""
Seek ->  Movimenta o cursor pelo texto, de acordo com o índice informado


--------------------------------------------------------------------------------------------------------------------
#  Exemplo Função Seek()

arq = open('file.txt')
print(arq.read())
print()
print(arq.read())  # vai abrir em branco, porque o cursor está no final
arq.seek(0)
print(arq.read())

--------------------------------------------------------------------------------------------------------------------
#  Exemplo Função readline() - Lê o arquivo linha por linha

arq = open('file.txt')
ret = arq.readline()
ret2 = arq.readline()
ret3 = arq.readline()
ret4 = arq.readline()
print(type(ret))
print(ret)
print(ret2)
print(ret3)
print(ret4)

--------------------------------------------------------------------------------------------------------------------
#  Exemplo Função readlines() - Lế tudo e coloca dentro de uma lista, onde cada item é uma linha

arq = open('file.txt')
ret = arq.readlines()
print(ret)

--------------------------------------------------------------------------------------------------------------------


OBS.:  Quando se abre um arquivo com a função open(), cria-se uma conexão do arquivo com o programa.
    Esta é chamada de streaming e deve ser fechada após os trabalhos no aquivo, com a função .close()


open = abrir
read = leia
seek = procurar
with = com
closed = está fechado?

--------------------------------------------------------------------------------------------------------------------
#  Verificando se o arquivo está fechado

arq = open('file.txt')
ret = arq.readlines()
print(ret)
print(arq.closed)
arq.close()
print(arq.closed)


"""

