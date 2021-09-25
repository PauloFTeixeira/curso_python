"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado dos componentes deste vetor, 
armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprima todos os elementos.

"""
vetor = set(range(1, 11))
vetor1 = set({})
for numero in vetor:
    numero = numero ** 2
    vetor1.add(numero)
print(vetor)
print(vetor1)
