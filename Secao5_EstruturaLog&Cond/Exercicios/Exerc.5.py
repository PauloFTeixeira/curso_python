"""
Faça um programa que receba um número inteiro e verifique se este número é par ou impar.
"""
numero = int(input('Digite um número inteiro: '))
resto = numero % 2
if resto == 0:
    print(f'{numero} é par')
else:
    print(f'{numero} é impar')
