"""
Dica de quando e onde trator erro:
    - TODA ENTRADA DO USUÁRIO DEVE SER TRATADA

"""
#  Exemplo
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou o número {num}')

#  O else só entra se o except não for ativado

#  Exemplo com Finaly
try:
    num1 = int(input('Digite um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou o numero {num1}')
finally:
    print('Operação finalizada')

#  O Finally é sempre executado
#  Usado para finalizar ou desalocar recurso, como exemplo encerrar conexão com Banco de Dados


#  Exemplo Complexo


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
