"""
Leia um número real.
Se o número for positivo, imprima a raiz quadrada. Do contrário, imprima o numero ao quadrado.
"""
numero = int(input('Digite um número: '))
if numero > 0:
    raiz = numero ** (1/2)
    print(f'A raiz quadrada de {numero} é {raiz}.')
else:
    quadrado = numero ** 2
    print(f'O {numero} elevado ao quadrado é {quadrado}. ')
