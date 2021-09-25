"""
all() retorna verdadeiro se todos os elementos do iterável forem verdadeiros ou se o interável estiver vazio

EXEMPLO:
print(all([0, 1, 2, 3]))  #  False -> (0) representa False
print(all([1, 2, 3, 4]))  #  True
print(all([]))  #  True


nomes = ['Carlos', 'Carla', 'Cassiano', 'Cristiano']
print(all([nome[0] == 'C' for nome in nomes]))


any()  retorna verdadeiro se qualquer um dos elementos for verdadeiro

"""

