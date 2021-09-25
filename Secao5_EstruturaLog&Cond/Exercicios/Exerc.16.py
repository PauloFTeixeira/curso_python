"""
Usando switch, escreva um programa que um inteiro entre 1 e 12 e imprima o mês correspondente a este número.
"""
numero = int(input('Escreva um número inteiro de 1 a 12: '))
if numero == 1:
    print('Janeiro')
elif numero == 2:
    print('Fevereiro')
elif numero == 3:
    print('Março')
elif numero == 4:
    print('Abril')
elif numero == 5:
    print('Maio')
elif numero == 6:
    print('Junho')
elif numero == 7:
    print('Julho')
elif numero == 9:
    print('Agosto')
elif numero == 10:
    print('Outubro')
elif numero == 11:
    print('Novembro')
elif numero == 12:
    print('Dezembro')
else:
    print('Numero inválido')
