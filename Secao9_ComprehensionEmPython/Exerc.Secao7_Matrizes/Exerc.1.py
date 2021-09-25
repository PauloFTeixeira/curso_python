"""
Leia uma matriz 4x4, conte e escreva quantos valores maiores que 10 ela possui

print(len(matriz[0]))
print(len(matriz[1]))
print(len(matriz[2]))
print(len(matriz[2]))
"""
matriz = [[1, 2, 3, 4], [5, 6, 7, 9], [10, 11, 12, 13], [14, 15, 16, 17]]
#print(matriz)


maiores = [[x for x in lista if x > 10] for lista in matriz]
print(len(maiores))
print(maiores)







maior = max([valor for linha in m for valor in linha])

m = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input()))

    m.append(linha)

maior_linha = 0
maior_coluna = 0
maior = m[0][0]
for l in range(4):
    for c in range(4):        
        if maior < m[l][c]:
            maior = m[l][c]
            maior_linha = l
            maior_coluna = c

print('linha do maior: {}\ncoluna do maior: {}'.format(maior_linha, maior_coluna))