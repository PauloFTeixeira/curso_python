"""
Bastante parecidas com as listas

Existem duas diferenças

1º -> representadas por ()
2º -> sõa imutáveis, isso sinifica que ao criar uma tupla, ela não muda mais. Toda operação em uma tupla gerar outra.
---------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------
#  CUIDADOS 1: REPRESENTADO POR (), MAS VEJA BEM...
tupla1 = (1, 2, 3, 4)
print(tupla1)
print(type(tupla1))
tupla2 = 5, 6, 7, 8
print(tupla2)
print(type(tupla2))

#  CUIDADO 2: TUPLAS COM UM ELEMENTO
tupla3 = (4)  #  não é uma tupla
print(tupla3)
print(type(tupla3))
tupla4 = (4,)  #  é uma tupla
print(tupla4)
print(type(tupla4))
#  Conclusão: conclui-se que tuplas são definidas por VÍRGULA(,) e não por PARENTESE()

---------------------------------------------------------------------------------------------------------------------
#  CRIAR TUPLAS ATRAVÉS DO RANGE
tupla = tuple(range(11))
print(tupla)

---------------------------------------------------------------------------------------------------------------------
#  DESEMPACOTANDO TUPLAS
tupla = ('Geek', 'Programação')
escola, curso = tupla
print(escola)
print(curso)
#  OBS.: como nas listas, deve conter o mesmo numero de elementos e variáveis, senão causa erro

---------------------------------------------------------------------------------------------------------------------
#  MÉTODOS DE ADIÇÃO E REMOÇÃO DE ELEMENTOS EM TUPLAS

Não existem, pelo fato de serem imutáveis

---------------------------------------------------------------------------------------------------------------------
#  CONCATENAÇÃO DE TUPLAS
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(tupla1, tupla2)
#         concat.
print(tupla1+tupla2)
print(tupla1, tupla2)
#                     OU
tupla3 = tupla1+tupla2
print(tupla3)
#                    OU AINDA
tupla1 = tupla1+tupla2  #  são imutaveis, mas pode-se sobreescrever seu valor
print(tupla1)

---------------------------------------------------------------------------------------------------------------------
#  VERIFICAR SE DETERMINADO VALOR ESTÁ NA TUPLA
tupla = 1, 2, 3
print(4 in tupla)

---------------------------------------------------------------------------------------------------------------------
#  ITERANDO SOBRE TUPLA
tupla = 1, 2, 3
for num in tupla:  #  TRADUÇÃO: para cada numero na tupla, imprima ele
    print(num)
for indice, valor in enumerate(tupla):
    print(indice, valor)

---------------------------------------------------------------------------------------------------------------------
#  CONTANDO ELEMENTOS DENTRO DE UMA TUPLA
tupla = ('a', 'b', 'c', 'd', 'e', 'f', 'a')
print(tupla.count('a'))

---------------------------------------------------------------------------------------------------------------------
#  DICAS DE UTILIZAÇÃO DE TUPLAS

Deve-se utilizar tuplas SEMPRE que não precisar modificar os dados contidos em uma coleção.

Ex.: meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

---------------------------------------------------------------------------------------------------------------------
#  ACESSO A ELEMENTOS DE UMA TUPLA
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses[4])
#          ind.

---------------------------------------------------------------------------------------------------------------------
#  ITERAR COM WHILE

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

while indice < len(meses):
    print(meses[indice])
    indice = indice+1

---------------------------------------------------------------------------------------------------------------------
#  VERIFICAR EM QUAL INDICE UM ELEMENTO ESTÁ

tupla = (1, 2, 3, 4, 5)
#                elem.
print(tupla.index(2))
#  se caso não existir, vai gerar um erro

---------------------------------------------------------------------------------------------------------------------
#  SLICING (MESMA COISA DAS LISTAS)
tupla[inicio:fim:passo]

---------------------------------------------------------------------------------------------------------------------
#  PORQUE USAR TUPLAS
-> mais rápida
-> deixam o código mais seguro (elementos imutáveis trazem segurança para o código)

---------------------------------------------------------------------------------------------------------------------
#  COPIANDO UMA TUPLA PARA OUTRA
tupla = 1, 2, 3
print(tupla)
nova = tupla
print(nova)
#  OBS.: na tupla, não existe Shallow Copy

---------------------------------------------------------------------------------------------------------------------

"""


