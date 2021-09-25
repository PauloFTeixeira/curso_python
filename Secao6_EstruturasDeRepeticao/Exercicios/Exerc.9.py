"""
Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.
"""
numero = int(input('Digite um número inteiro: '))
print(f' O número digitado foi {numero}')
for n in range(1, numero + 1, 2):
    print(f' Antes de {numero} ainda tem o númeoro impar {n}.')



