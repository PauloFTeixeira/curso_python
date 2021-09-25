"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""
qtd = 10
valores = []

for n in range(1, qtd + 1):
    num = int(input(f'Digite o valor {n}/{qtd}: '))
    valores.append(num)

print(f'O maior valor é {max(valores)}.')
print(f'O menor valor é {min(valores)}.')
