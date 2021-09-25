"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
crescente.
"""
numero = int(input('Digite um némero inteiro: '))
if (numero % 2) == 0:
    for n in range(0, numero, 2):
        print(n)
