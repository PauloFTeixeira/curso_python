"""
Listas aninhadas - (nested list)

Em algumas linguagens, tem-se arrays (C, Java)
- Unidimensional (arrays/vetores)
- Multidimensionais (matrizes)

Em python, se tem as listas aninhadas


Exemplo:

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Obs.: Cada sublista é uma linha
      Cada numero é uma coluna

Acesso aos dados

    print(lista[linha][coluna])

------------------------------------------------------------------------------------------------------------------
#  ACESSANDO DADOS
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista[0][0])

------------------------------------------------------------------------------------------------------------------
#  ITERANDO COM LOOP EM LISTA ANINHADA

for list in lista:
    for num in list:
        print(num)

------------------------------------------------------------------------------------------------------------------
#  LIST COMPREHENSION
[[print(valor) for valor in list]for list in lista]

#  OBS.: toda instrução comprehension, se lê de trás pra frente

------------------------------------------------------------------------------------------------------------------
"""

#  OUTROS EXEMPLOS
#  GERANDO UM TABULEIRO/MATRIZ 3X3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)


#  GERANDO JOGADAS DE JOGO DA VELHA

velha = [['x' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)









