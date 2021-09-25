"""
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:

a = (base maior + base menor) * altura / 2
"""

bmaior = float(input('Informe a base maior de um trapézio: '))
if bmaior > 0:
    bmenor = float(input('Informe a base menor do trapézio: '))
    if bmenor > 0:
        alt = float(input('Informe a altura do trapézio: '))
        area = ((bmaior * bmenor) * alt) // 2
        print(f' A area do trapézio é de {area}')
else:
    print('Dado incorreto!')
