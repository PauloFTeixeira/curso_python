"""
Leia um vetor de 10 posições. Contar e escrever quantos valores pares possui
"""

vetor = range(1, 11)
par = []
for n in vetor:
    if n % 2 == 0:
        par.append(n)

print(len(par))
print(par)
