"""
#  SEMPRE LEMBRAR DE USAR HELP, TEM MUITA INFORMAÇÃO BOA

Listas em Python funcionam como VETORES/MATRIZES (arrays) em outras linguagens, com a diferença de serem DINAMICAS
e também pode-se colocar qualquer tipo de dado.
    - C e Java -> possuem tamanho e tipo fixo;
    - Python -> tamanho infinito (o que a memória suportar) e aceita qualquer tipo de dado;

OBS.: Listas são representadas por []
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
#     EXEMPLOS DE USO DE LISTAS!!!                                    EXEMPLOS DE USO DE LISTAS!!!
---------------------------------------------------------------------------------------------------------------------
Exemplo: lista = [1, 2,'a']

#  PODE-SE CHECAR SE DETERMINADO VALOR ESTÁ NA LISTA.

lista1 = [1, 2, 3, 4, 5]
num = 11
if num in lista1:  # TRADUÇÃO - se num está dentro da lista:
    print(f'Contem {num}')
else:
    print(f'Não contém {num} nesta lista.')

---------------------------------------------------------------------------------------------------------------------
# PODE-SE ORDENAR UMA LISTA
lista1 = [12, 55, 23, 466, 343, 564, 435, 633, 7867, 244]
lista1.sort()
print(lista1)

---------------------------------------------------------------------------------------------------------------------
#  PODE-SE CONTAR QUANTAS OCORRÊNCIAS DE UM VALOR DA LISTA
lista = [1, 2, 3, 4, 1, 2]
print(lista)
print(lista.count(3))

---------------------------------------------------------------------------------------------------------------------
#  ADICIONAR UM VALOR - APPEND
#  Para adicionar novos valores, usa-se a função 'APPEND'
lista = [1, 2, 3, 4, 1, 2]
print(lista)
lista.append(10)
print(lista)
#  Append adiciona somente um valor por vez!!!
# Mas é possivel, com append, colocar um lista dentro da outra
lista.append([11, 12, 13])
print(lista)

---------------------------------------------------------------------------------------------------------------------
# ADICIONAR VARIOS VALORES DE UMA VEZ - EXTEND
lista = [1, 2, 3, 4, 1, 2]
print(lista)
lista.extend([11, 13, 14])
print(lista)
#  os valores são adicionados sempre no final da lista

---------------------------------------------------------------------------------------------------------------------
#  ADICIONAR NOVO VALOR, INFORMANDO INDICE (POSIÇÃO) QUE DEVE FICAR O NOVO VALOR NA LISTA
lista = [1, 2, 3, 4, 1, 2]
print(lista)
#          ind.  val.
lista.insert(2, 4444)
print(lista)

---------------------------------------------------------------------------------------------------------------------
#  JUNTAR DUAS LISTAS OU MAIS
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
print(lista1)
print(lista2)
lista3 = lista1 + lista2
print(lista3)
#         OU
lista1.extend(lista2)
print(lista1)

---------------------------------------------------------------------------------------------------------------------
#  INVERTER UMA LISTA
lista = [1, 2, 3, 4]
lista.reverse()
print(lista)
#          ou com slicing
print(lista[::-1])  # não está funcionando

---------------------------------------------------------------------------------------------------------------------
#  COPIAR UMA LISTA
lista = [1, 2, 3, 4]
lista2 = lista.copy()
print(lista2)
lista.append(5)
print(lista)
print(lista2)
#  com o 'copy', com a alteração de uma lista não interfere na outra.

---------------------------------------------------------------------------------------------------------------------
#  VER O TAMANHO DE UMA LISTA (QUANTOS ELEMENTES EXISTEM NELA)

lista = [1, 2, 3, 4]
print(len(lista))


---------------------------------------------------------------------------------------------------------------------
#  VER O TAMANHO DE UMA LISTA (QUANTOS ELEMENTES EXISTEM NELA)

lista = [1, 2, 3, 4]
print(len(lista))

---------------------------------------------------------------------------------------------------------------------
#  REMOVER O ULTIMO ELEMENTO DA LISTA

lista = [1, 2, 3, 4]
print(lista)
lista.pop()  #  ou print(lista.pop())
print(lista)

---------------------------------------------------------------------------------------------------------------------
#  REMOVER ELEMENTO PELO INDICE QUE SE ENCONTRA - indice começa sempre em 0

lista = [1, 2, 3, 4]
print(lista)
lista.pop(2)
#        ind.
print(lista)
#  OBS.: se nao houver elemento no indice informado, da erro
---------------------------------------------------------------------------------------------------------------------
#  REMOVER TODOS ELEMENTOS DA LISTA

lista = [1, 2, 3, 4]
print(lista)
lista.clear()
print(lista)

---------------------------------------------------------------------------------------------------------------------
#  MULTIPLICAR LISTA

lista = [1, 2, 3, 4]
print(lista)
lista2 = lista * 3
print(lista2)
#  repete quantas vezes informar, um lista em outra

---------------------------------------------------------------------------------------------------------------------
#  CONVERTER STRING EM LISTA

nome = 'Paulo Fernando'
lista = nome.split()
print(lista)
#  por padrão, split separa os elementos pelo 'ESPAÇO' entre elas.

# pode-se indicar o separador
nome1 = "Lopes,Teixeira"
lista1 = nome1.split(',')
#                   separ.
print(lista1)
#  sempre informar o separador entre 'aspas'
---------------------------------------------------------------------------------------------------------------------
#  CONVERTER STRING EM LISTA

lista = ['Paulo', 'Fernando']
nome = ' '.join(lista)  #  TRADUÇÃO: pega a lista, colocar um espaço entre os elementos e transforma em um string.
print(lista)
print(nome)

---------------------------------------------------------------------------------------------------------------------
#  ITERAR SOBRE LISTA

#  EXEMPLO 1: usando for

lista = [1, 2, 3, 4]
for elemento in lista:  #  TRADUÇÃO: para cada elemento dentro da lista, imprima ele
    print(elemento)
#                   OU
soma = 0
for elem in lista:
    soma = soma+elem
print(soma)

# EXEMPLO 2: usando while
produto = []
carrinho = []
while produto != 'sair':
    print("Adicione um produto ou digite 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

---------------------------------------------------------------------------------------------------------------------
#  UTILIZANDO VARIÁVEL EM LISTAS
num1 = 1
num2 = 2
num3 = 3
numeros = [num1, num2, num3]
print(numeros)

---------------------------------------------------------------------------------------------------------------------
#  ACESSO AOS ELEMENTOS DE FORMA INDEXADA

#  ind.     0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[2])

---------------------------------------------------------------------------------------------------------------------
#  ACESSO AOS ELEMENTOS DE FORMA INDEXADA, DE TRÁS PRA FRENTE

#  ind.     0         1        2        3
#  ind.(-) -4        -3       -2       -1
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[-1])
print(cores[-2])
#  para entender melhor o conceito de trás pra frente, pensar na lista como um círculo, onde anntes do 0, vem -1.

---------------------------------------------------------------------------------------------------------------------
#  GERAR OS INDICES DA LISTA COM FOR

cores = ['verde', 'amarelo', 'azul', 'branco']
for indice, cores in enumerate(cores):
    print(indice, cores)

"""
#  ------------------------------------------------------------------------------------------------------------------
"""
                           OUTROS MÉTODOS
---------------------------------------------------------------------------------------------------------------------
#  ENCONTRAR O INDICE DE UM ELEMENTO NA LISTA

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num)
print(num.index(10))  #  TRADUÇÃO: em que índice está o valor 10?
#              valor
#  se houver valor duplicado, vai retornar o índice do primeiro valor

---------------------------------------------------------------------------------------------------------------------                                                     
#  FAZER BUSCA DE ÍNDICE DENTRO DO RANGE - INFORMANNDO O INDICE DE COMEÇO DA BUSCA

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#             valor
print(num.index(5, 3))
#                  ind. de começo da busca

---------------------------------------------------------------------------------------------------------------------
#  FAZER BUSCA DE ÍNDICE DENTRO DO RANGE - INFORMANNDO O INDICE DE COMEÇO E FIM DA BUSCA

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#           valor     ind. fim da busca
print(num.index(2, 3, 10))
#                 ind. de começo da busca

---------------------------------------------------------------------------------------------------------------------
#  REVISÃO DE SLICING

#  lista(range[inicio:fim:passo])
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  slicing de inicio
print(num[2:])
# slicing de fim
print(num[:5])
#  slicing de passo
print(num[::2])
# o começo padrão do slicing é sempre 0

---------------------------------------------------------------------------------------------------------------------
#  INVERTENDO VALORES EM UMA LISTA

nomes = ['Paulo', 'Fernando']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
#               OU
nome = ['Paulo', 'Fernando']
nome.reverse()
print(nome)

---------------------------------------------------------------------------------------------------------------------
#  SOMA*, VALORES MÁXIMO*, VALOR MÍNIMO*, TAMANHO
#  * -> marcados com * devem ser obrigatóriamente valores inteiro ou real
num = [1, 2, 3, 4, 5]
print(sum(num))  #  soma
print(max(num))  #  máximo
print(min(num))  #  mínimo
print(len(num))  #  tamanho

---------------------------------------------------------------------------------------------------------------------
#  DESEMPACOTANDO UMA LISTA

lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
#  OBS.: se tiver mais valor que variável ou mais variável que valor, vai dar erro.

---------------------------------------------------------------------------------------------------------------------
#  COPIANDO UMA LISTA PARA OUTRA  (SHALOW COPY) & (DEEP COPY)

# Deep Copy
lista = [1, 2, 3]
print(lista)
nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)
# Neste caso, alterações em uma das listas não irá afetar na outra (estão independentes)

# Shalow Copy

lista1 = [1, 2, 3]
print(lista1)
nova1 = lista1
nova1.append(4)
print(lista1)
print(nova1)
# Nesta caso, alterando uma lista, altera a outra.

"""





