"""
Generators são iterators, mas não ao contrário

Outras informações:
- Generators podem ser criados com funções geradoras
- Funções geradores usam a palavras reservada yield
- Generators podem ser criados com expressões geradoras

FUNÇÕES:
Usam return
Retornam uma vez
Retorna um valor

FUNÇÕES GERADORAS:
Usam yield
Podem retornar várias vezes
Retornam um generator

Exemplo:
def conta_ate(valor):
    contador = 1
    while contador <= valor:
        yield contador
        contador = contador + 1
    raise StopIteration


#  Uma função geradora não um generator, ela retorna um
n = conta_ate(5)
print(next(n))
print(next(n))
print(next(n))
print(next(n))

"""
