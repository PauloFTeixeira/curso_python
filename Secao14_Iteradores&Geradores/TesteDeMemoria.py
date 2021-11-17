"""
Comparação do uso de memória para executar as funções

"""

#  Sequencia de Fibonacci
#  1,1,2,3,5,8,13

#  Função Comum


def fib(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


for n in fib(100000):
    print(n)
#  Uso de 449 MB de memória para executar a função


#  Função Geradora


def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


for n in fib_gen(100000):
    print(n)
#  Uso de 3 MB de memória para executar a função
