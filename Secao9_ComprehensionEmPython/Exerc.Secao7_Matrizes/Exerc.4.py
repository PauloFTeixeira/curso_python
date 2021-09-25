"""
Leia uma matriz 4x4, imprima a matriz e retorne a localização (linha e coluna) do maior valor
"""

m = 2
#  Estruturando matriz
matriz = [[0 for x in range(m)]for x in range(m)]
for i in range(0, m):
    for j in range(0, m):
        print(f'{matriz[i][j]} ', end='')  # O END='' serve para impedir que cada elemente seja quebrado a linha
    print()

#  Inserindo dados na matriz
for i in range(0, m):
    for j in range(0, m):
        matriz = int(input((f'Digite o valor {i}/{j}: ')))

        
#  Descobrindo a localização do maior valor
maiorl = 0
maiorc = 0

#  maiorl = matriz.index(max(x for l in matriz))
maiorl = matriz.index(max(x for l in matriz))



#maior_linha = matriz.index(max(matriz))
#maior_coluna = matriz[maior_linha].index(max(matriz[maior_linha]))
#print(f'localização maior valor: ({maior_linha}, {maior_coluna})')
