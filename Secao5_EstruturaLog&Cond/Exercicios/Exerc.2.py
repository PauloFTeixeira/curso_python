"""
Leia um numero fornecido pelo usuário. Se esse número é positivo, calcule a raiz quadrada do numero.
Se o numero for negativo, mostre uma mensagem dizendo que o numero é inválido.
"""
numero = float(input('Digite um número. '))
if numero > 0:
    raiz = numero ** (1/2)
    print(f'A raiz quadrada de {numero} é {raiz}')
else:
    print('Número inválido!')

          


