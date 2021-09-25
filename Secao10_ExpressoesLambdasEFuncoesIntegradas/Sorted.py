"""
Sort -> apenas faz a ordenação dentro de listas
Sorted -> Faz ordenação dentro de qualquer iterável, com a diferença que;
    Não modifica o original, ele gera uma lista com os valores ordenados

"""

#  Exemplo
numeros = [1, 5, 3, 8, 7, 8, 13, 14, 69, 47]  # poderia ser tupla ou set, qualquer coisa
print(sorted(numeros))

#  Exemplo com parâmetro
print(sorted(numeros, reverse=True))  #  ordenando do maior ao menor


