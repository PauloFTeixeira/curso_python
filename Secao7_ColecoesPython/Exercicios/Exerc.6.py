"""
Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior e o
menor elemento do vetor
"""
vezes = 10
numeros = []
for n in range(1, vezes + 1):
    num = int(input(f'Digite o valor {n}/{vezes}: '))
    numeros.append(num)

print(min(numeros))
print(max(numeros))
