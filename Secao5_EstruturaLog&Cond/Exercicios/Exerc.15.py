"""
Usando Switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este
numero. Isto é, domindo se 1, segundo se 2 e assim por diante.
"""

numero = int(input('Digite um numero de 1 a 7: '))
if (numero < 1) or (numero > 7):
    print('Numero inválido')
elif numero == 1:
    print('Domingo')
elif numero == 2:
    print('Segunda-feira')
elif numero == 3:
    print('Terça-feira')
elif numero == 4:
    print('Quarta-feira')
elif numero == 5:
    print('Quinta-feira')
elif numero == 6:
    print('Sexta-feira')
elif numero == 7:
    print('Sábado')
else:
    print('Número inválido')
