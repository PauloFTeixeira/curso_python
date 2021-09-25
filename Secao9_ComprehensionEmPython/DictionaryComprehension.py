"""
Sintaxe {chave:valor for valor in iterável}

--------------------------------------------------------------------------------------------------------------------
#  EXEMPLO

numeros = {'a': 1, 'b': 2, 'c:': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

--------------------------------------------------------------------------------------------------------------------
#  EXEMPLO

numeros = [1, 2, 3, 4]  #  pode ser lista, tupla, set
quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)

--------------------------------------------------------------------------------------------------------------------
#  EXEMPLO COM LÓGICA CONDICIONAL

numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)

--------------------------------------------------------------------------------------------------------------------
"""

