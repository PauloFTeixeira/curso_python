"""
Funções de maior grandeza - Higher Order Functions (HOF)

Quando uma linguagem suporta HOF, indica que podemos ter funções que retornam
outras funções como resultado, ou mesmo que podemos passar funções como parâmetro
de outras funções

#  Retornando uma função

def soma(a, b):
    return a + b


def diminui(a, b):
    return a - b


def calcula(num1, num2, funcao):
    return funcao(num1, num2)


print(calcula(2, 2, soma))

"""

#  NESTED FUNCTION (função aninhada)


def cumprimenta_pessoa(pessoa):
    def humor():
        return "E ai "

    return humor() + (pessoa)


print(cumprimenta_pessoa("Paulo"))
