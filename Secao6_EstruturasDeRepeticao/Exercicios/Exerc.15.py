"""
Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N em ordem
crescente
"""
numero = int(input('Digite um número inteiro: '))
if (numero % 2) != 0:
    for n in range(1, numero, 2):
        print(n)
