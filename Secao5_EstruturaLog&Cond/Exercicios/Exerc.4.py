"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
- O número digitado ao quadrado
- A raiz quadrada do número digitado
"""
numero = int(input('Digite um número: '))
if numero > 0:
    quadrado = numero ** 2
    raiz = numero ** (1/2)
    print(f'O {numero} ao quadrado é {quadrado} e sua raiz quadrada é {raiz}')
else:
    print('Tente novamente')
