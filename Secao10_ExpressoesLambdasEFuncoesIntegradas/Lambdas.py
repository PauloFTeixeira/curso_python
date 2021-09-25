"""
Expressões Lambdas: são funções sem nome ou também, anônimas.

                Exemplo de Função Comum

def funcao(x):
    return 3 * x + 1

                Exemplo de Função Lambda
lambda x: 3 * x + 1

   lambda x:             3 * X + 1
#  entrada              retorno


"""

#  Pode-se ter lambdas com multiplas entradas:

nome_completo = lambda nome, sobrenome: nome.strip().title() + (' ') + sobrenome.strip().title()

print(nome_completo('paulo', 'fernando'))
#  Pode-se ter lambdas com 1 ou mais entradas:
#  Ex. sintaxe: n = lambda x1, x2, x3...: <expressão>

# Outro exemplo: (ordenando pela ordem do sobrenome)
nomes = ['Paulo Teixeira', 'Paulo Lopes', 'Eduarda Santos']
nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(nomes)
#  Obs.: Maneira correta de usar lambda

#  Função Quadrática
#  f(x) = A * X ** 2 + B * X + C
def funvao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c
#                         argum.
print(funvao_quadratica(2, 3, 4)(2))
#                                valor de x


