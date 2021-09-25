"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
"""
soma = 0
for n in range(0, 51, 2):
    soma = soma + n
    print(n)
print(soma)
