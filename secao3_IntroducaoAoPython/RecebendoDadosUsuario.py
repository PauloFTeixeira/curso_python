"""
Print - imprimi na tela o que for escrito
Input - Solicita resposta do usário

    MODO ANTIGO DE PRINT
        print("Qual seu nome? ")
        nome=input()
        print('Seja bem-vindo(a) %s' %nome)

    MODO DE PRINT MODERNO
        print("Qual seu nome? ")
        nome=input
        print('A {0} tem {1} anos'. format (nome, idade))

    MODO DE PRINT ATUAL
        print("Qual seu nome? ")
        nome=input
        print(f'Seja bem vindo {nome}')  # o "f'" serve para que a função entre{} funcione

    MODO SIMPLIFICADO
        nome=input('Qual seu nome? ')
        idade=input('Qual sua idade? ')

"""
# Em Python, tudo que estiver entre "" é uma 'STRING'
# Todo dado recebi de um INPUT é uma STRING

''' CAST é a conversão de um tipo de dado para outro
    Ex. int(idade) -> TRANSFORMA A VARIAVEL EM NUMERO INTEIRO
'''

