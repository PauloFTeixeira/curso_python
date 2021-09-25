"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
decrescente.
"""
numero = int(input('Digite um némero inteiro: '))
if (numero % 2) == 0:
    for n in range(numero, 0, -2):
        print(n)
