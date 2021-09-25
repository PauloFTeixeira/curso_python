"""
Criação e manipulação de matrizes

sintaxe:
    matriz = [[0 for x in range(numero de colunas)]for x in range(numero de linhas)]

"""
#  Criando a estrutura da matriz:
lin = int(input('Quantas colunas vai ter? '))
col = int(input('Quantas linhas vai ter? '))

matriz = [[0 for x in range(col)]for x in range(lin)]

print(matriz)


# Inserindo dados na estrutura:
for i in range(0, col):
    for j in range(0, lin):
        matriz[i][j] = int(input(f'Digite o valor [{i}/{j}]: '))
print(matriz)
print()

#  Percorrendo os dados na estrutura matriz
print('Matriz:')
for i in range(0, lin):
    for j in range(0, col):
        print(f'{matriz[i][j]} ', end='')  # end='' para não deixar pular a linha
    print()  # print() para quebrar a linha após percorrer cada linha

#  Mostrando a diagonal principal

for i in range(0, col):
    print(f'{matriz[i][i]} ', end='')