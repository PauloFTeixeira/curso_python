"""
                        !!!   Vem a ser as tuples Compreensions  !!!

Ocupa bem menos espaço em memória, pois não gera o resultado e guarda em memória. Generation gera um objeto
que só vai gerar o resultado quando for ser usado.

Sua diferença da list Compreension é mínima



nomes = ['Carlos', 'Cassiano', 'Cristiano', 'Vanderlei']

#  List Compreension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

#  Generator
res1 = (nome1[0] == 'C' for nome1 in nomes)
print(type(res1))
print(res1)


#  A diferença de List Compreension e Generator é que em list se usa [] e em generator se usa ()

"""

