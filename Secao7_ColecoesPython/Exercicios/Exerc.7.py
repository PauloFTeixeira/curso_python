"""
Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento
e a posição que ele se encontra

"""

num = [25, 258, 147, 236, 185, 147, 1236, 14782, 8554, 145]
 
maior = (max(num))
indice = num.index(maior)
print(f'O maior numero e {maior} e esta localizado no indece {indice}')
 
 