"""
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y, quaisquer 
correspondente a duas posições do vetor. Ao final seu programa deverá escrever a soma dos valores encontrados
nas respectivas posições X e Y.

"""
qtd = 8
lista = []
for n in range(1, qtd + 1):
    num = int(input(f'Informe o número {n}/{qtd}: '))
    lista.append(num)

ind = 2
ind1 = []
for n1 in range(1, ind + 1):
    num1 = int(input(f'Digite o índice {n1}/{ind}: '))
    ind1.append(num1)



soma = lista[ind1[0]] + lista[ind1[1]]
print(soma)


#  Exercício não ficou bem resolvido, lógica ficou ruim!!!
