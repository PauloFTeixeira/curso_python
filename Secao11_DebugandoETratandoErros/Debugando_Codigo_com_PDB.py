"""
PDB -> Python Debugger
Bug -> Inseto

Debugar com print não é uma boa prática


-------------------------------------------------------------------------------------------------------------------
#                                       USANDO PYCHARM


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        print('Valor não aceito')
    except ZeroDivisionError:
        print(f'Não tem como dividir por 0')


num2 = int(input('Digite um número: '))
num3 = int(input('Digite outro número: '))
dividir(num2, num3)

--------------------------------------------------------------------------------------------------------------------

"""


#                                       USANDO PDB
#  Debugação manual
#  Preciso importar a biblioteca pdb e usar a função set_trace()
#       l -> listar localização no código
#       n -> próxima linha
#       p -> imprimir variáveis
#       c -> coninuar a execução - Finaliza o Debbuging

import pdb
nome = 'Paulo'
sobrenome = 'Teixeira'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = ' Programação em Python '
final = nome_completo + 'faz o curso' + curso

print(final)
