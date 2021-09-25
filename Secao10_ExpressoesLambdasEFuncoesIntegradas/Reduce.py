"""
A partir do Python 3+ a função REDUCE não é mais uma função integrada (built-in). Agora é previso importar e
usa-la a partir do módulo (functools)

É preferivel usar um loop for, por ser mais legível

--------------------------------------------------------------------------------------------------------------------
#  Em uma coleção:
num = [1, 2, 3, 4, 5, 6, 7, 8]

#  Uma função com dois parâmetro:


def funcao(x, y):
    return x * y


#  Assim como map e filter, recebe dois parâmetros: <função, iterável>

#  Reduve funciona da seguinte forma:
#  PASSO 1

#  res1 = função(a1, a2)  aplica a função aos dois primeiros elementos da coleção e guarda o resultado
#  PASSO 2
#  res2 = função(res, a3)  apliva a função aplicando o resultado do passo anterior e o próximo elemento, repetindo
#  até o final
from functools import reduce
resp = reduce(funcao, num)
print(resp)

"""
from functools import reduce

lista = [23, 85, 47, 36, 89, 47, 42, 53, 58]

mult = lambda x, y: x * y
res = reduce(mult, lista)
print(res)


#  Usando Loop comum

resp = 1
for n in lista:
    resp = resp * n

print(resp)

