"""
Escreve um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença
existente entre eles
"""
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    dif1 = num1 - num2
    print(f'{num1} é maior, com diferença de {dif1}')
else:
    dif2 = num2 - num1
    print(f'{num2} é maior, com diferença de {dif2}')
