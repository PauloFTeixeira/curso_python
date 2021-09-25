"""
Faça um programa que leia 10 numeros positivos, ignorando não positivos, e imprima sua média.
"""
qtd = 10
soma = 0
for n in range(1, qtd + 1):
    num = int(input(f'Digite o {n}/{qtd}: '))
    if num > 0:
        soma = soma + num
media = soma / qtd
print(f'A média dos numeros é {media}')
