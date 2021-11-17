"""
Iterators:
- Objeto que permite ser iterado
- Objeto que retorna um dado, sendo um elemento por vez, quando uma função next for chamada

Iterable:
- Objeto que irá retornar um iterator

Todo iterator é um iterable, mas não vise versa

#  Exemplo de iterable, mas não é iterator
nome = 'Paulo'
nums = [1, 2, 3, 4]

# Transformar em iterator
it = iter(nome)
it2 = iter(nums)

"""
nome = 'Paulo'
nums = [1, 2, 3, 4]

it1 = iter(nome)
it2 = iter(nums)

print(next(it1))
print(next(it1))
