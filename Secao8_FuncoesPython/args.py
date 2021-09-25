"""
*args

- O *args é um parâmetro como qualquer outro, isso significa que pode se chamar de qualquer coisa, desde que
comece com asterisco (*).
Ex.: *x, mas no geral, é usado *args

O parâmetro *args usado em uma função, coloca os valores extra informados como entrada em um tupla.

OBS.: Usa-se * na definição, na execução não usa *

--------------------------------------------------------------------------------------------------------------------
                                       #  SEM USAR *ARGS
def numeros(num1, num2, num3):
    return num1 + num2 + num3


print(numeros(1, 2, 3))


                                       #  USANDO *ARGS

def num(*args):
    return sum(args)


print(num(1, 2, 3))

--------------------------------------------------------------------------------------------------------------------
#  ENTENDENDO O *ARGS


def soma(nome, sobrenome, *args):
    return sum(args)


print(soma('Paulo', 'Teixeira', 1, 2, 3, 4))

--------------------------------------------------------------------------------------------------------------------
#  DESEMPACOTAMENTO

num = [1, 2, 3, 4, 5]


def soma(*args):
    return sum(args)


print(soma(*num))

--------------------------------------------------------------------------------------------------------------------
"""