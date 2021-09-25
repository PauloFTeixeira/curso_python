"""
Crie um programa que lê 6 valores inteiros e , em seguida, mostre na tela os valores lidos.

"""
numVal = 6
valores = []
for n in range(1, numVal + 1):
    num = int(input(f'Digite o valor {n}/{numVal}: '))
    valores.append(num)
print(valores)


