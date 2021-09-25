"""
Faça um programa que leia 10 inteiros e imprima sua média.
"""
qtd = int(input('Informe o número de dados: '))
soma = 0
for n in range(1, qtd + 1):
    num = float(input(f'Informe o valor {n}/{qtd}: '))
    soma = soma + num
    print(soma)
media = float(soma / qtd)
print(f'A média dos valores é {media}. ')
