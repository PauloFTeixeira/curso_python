"""
- Sção pequenas partes de código que realizam tarefas específicas
- Pode ou nõa receber entrada de dados e retornar uma saída de dados
- Muito úteis para para executar procedimentos similares por repetidas vezes

OBS.: Se a função realiza várias tarefas dentro dela, é bom fazer uma verificação para que a função seja simplificada

Exemplos.:  print('Olá mundo')
#          função

lista = []
lista.append(1)
#     função


Funções integradas do Python são chamadas de Built-in, Ex.: print(), lem)(), append() e outras...

Conceito DRY -> Don't repeat yourself (não repita voçe mesmo / não repita seu código)

DEFINIÇÃO DE FUNÇÕES:

def nome_da_função(parâmetro_de_entrada)
    bloco da função

ONDE:
Nome da função: sempre minúsculo, se for composto separar com underline (_)
Parâmetro de entrada: Opcional, se for mais de um separar com vírgula (,), podendo ser opcional ou não
Bloco da função: Onde o processamento acontece, pode ter ou não retorno da função. Identado com 4 espaços

Abre-se a função com a palavra reservada  "def"


def diz_oi():
    print('Oi!')

diz_oi()
---------------------------------------------------------------------------------------------------------------------
#  FUNÇÕES COM RETORNO
#  Exemplo de função com retorno

lista = [1, 2, 3]
lista.pop()
ret_pop = lista.pop()
print(f'O retorno de pop é: {ret_pop}')

#  Exemplo de função sem retorno

lista = [1, 2, 3]
ret_print = print(lista)
print(f'O retorno do print é: {ret_print}')  #  Retorno é none

#  OBS.: Em python, quando a funçao não tem retorno, o valor é none
#  OBS.: Funções python que retornam valores, devem retornar esses valores com a palavras reservada "return"

---------------------------------------------------------------------------------------------------------------------
#  Exemplo - Sem retorno


def quadrado_de_7():
    print(7 * 7)
    ret = quadrado_de_7
    print(ret)

---------------------------------------------------------------------------------------------------------------------
#  Exemplo - Com retorno


def quadrado_de_sete():
    return 7 * 7


quadrado_de_7()

print(quadrado_de_sete())

OBS.: Não é obriatório criar variável para receber o retorno, pode-se passar a execução da função para outra
função

---------------------------------------------------------------------------------------------------------------------
#  Return é bom para se juntar o retorno com outras partes do código

alguem = 'Paulo Fernando'

def oi():
    return 'Oi '


print(oi() + alguem)

---------------------------------------------------------------------------------------------------------------------
#  Observações sobre a palavras "return"

1 - Ela finaliza a função
2 - Pode-se ter vários return em uma função
3 - Pode-se, em uma função, retornar qualquer tipo de dado e até mesmo multiplicar valores

#  Exemplo 1 - return finaliza a função
def oi():
    return 'Oi'
    print('Olá')  #  não vai exexutar, porque finalizou no return
print(oi())

---------------------------------------------------------------------------------------------------------------------
#  Exemplo 2 - vários return

def nova():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'B'


print(nova())

---------------------------------------------------------------------------------------------------------------------
#  Exemplo 3 - retornar qualquer tipo de dado


def outra():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra()
print(num1, num2, num3, num4)

---------------------------------------------------------------------------------------------------------------------
#  Função jogar CARA OU COROA

from random import random


def jogar_moeda():
   valor = random()
   if valor > 0.5:
        return 'Cara'
   return 'Coroa'


print(jogar_moeda())

---------------------------------------------------------------------------------------------------------------------
"""

















