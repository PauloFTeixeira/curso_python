"""
Faça um programa que receba dois numeros e mostre o maior. Se por acaso os dois números forem iguais, imprima
a mensagem: Numeros iguais
"""
numero1 = int(input('Digite um numero inteiro: '))
numero2 = int(input('Digite outro numero inteiro: '))
if numero1 > numero2:
    print(f'{numero1} é o maior número')
elif numero1 < numero2:
    print(f'{numero2} é o maior número')
else:
    print('Números iguais')
