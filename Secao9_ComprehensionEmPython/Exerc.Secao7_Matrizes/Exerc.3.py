"""
Faça um programa que preencha uma matriz 4x4 com o produto do valor da linha e da coluna de cada elemento. 
Em seguida, imprima na tela a matriz

"""
m = 4
# montando matriz
matriz = [[0 for x in range(m)]for x in range(m)]
print(matriz)

#  Inserindo dados na matriz

for i in range(0, m):
    for j in range(0, m):
        matriz[i][j] = i + j

print(matriz)

#  Ajustando a exibição da matriz

for i in range(0, m):
    for j in range(0, m):
        print(f'{matriz[i][j]} ', end='')
    print()

