"""

"""

nome = 'Paulo'

for l in nome:
    print(l)

#  Criando uma versão de loop


def letra(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


#  Funciona da mesma maneira que o loop for
