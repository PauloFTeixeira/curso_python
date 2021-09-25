"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 ate N em ordem
crescente.
"""
soma = 0
n = int(input('Digite um némero inteiro: '))
if n >= 0:
    for num in range(0, n + 1):
        print(num)
