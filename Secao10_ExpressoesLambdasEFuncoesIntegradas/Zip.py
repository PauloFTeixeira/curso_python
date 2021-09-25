"""
Zip() -> cria um iterável (zip object), formando pares com cada elemento do 2 iteráveis passados


"""

l1 = [1, 2, 3]
l2 = [4, 5, 6]

zip1 = zip(l1, l2)
print(type(zip1))
print(zip1)
#  print(list(zip1))

"""
OBS.:  Some da memória após o primeiro uso
    Se estiver com iteráveis de tamanhos diferentes, ele considera o menor tamanho
"""
for t in zip1:
    print(list(t))


