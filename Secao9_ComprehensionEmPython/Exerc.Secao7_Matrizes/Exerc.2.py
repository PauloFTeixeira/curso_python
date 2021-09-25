"""
Declare uma matriz 5x5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a
matriz obtida
"""
lin = int(input('Quantas linhas: '))
col = int(input('Quantas colunas: '))
#  Criação de matriz
matriz = [[0 for x in range(0, lin)] for x in range(0, col)]

print(matriz)

#  Informando os valores de cada posição da matriz
for i in range(0, lin):
    for j in range(0, col):
        matriz[i][j] = float(input(f'Digite o valor [{i}/{j}]: '))

print(matriz)
#  Acessando a diagonal

for i in range(0, lin):
    print(f'{matriz[i][i]}', end='')
    print(' ')


#  Acessando maior e menor valor Valor da Matriz

maior = 0
menor = 0
m = [0][0]

for l in range(0, lin):
    for c in range(0, col):
        if matriz[l][c] == 0:
            maior = menor = matriz[l][c]
        else:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
            if matriz[l][c] < menor:
                menor = matriz[l][c]
print(f'O maior valor da matriz é {maior} e o seu vaor é {menor}')

#  Acessando o indice do maior e do menor valor
indMaior = 0
indMenor = 0

"""
print()
print(indMaior)
print()
print(indMenor)
"""
