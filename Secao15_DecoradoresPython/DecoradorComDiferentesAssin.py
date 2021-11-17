"""
Para resolver, usa-se um padrão de projeto chamado Decorator Patter

Serve para fazer verificação de valores


def verifica_primeiro_valor(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto, primeiro argumento tem que ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_valor('pizza')  # Primeiro valor informado na função, deve ser o passado nesse parâmetro
def comida_favorita(*args):
    return args


@verifica_primeiro_valor(10)  # Primeiro valor informado na função, deve ser o passado nesse parâmetro
def soma(num1, num2):
    return num1 + num2

print(comida_favorita('Churrasco'))  
print(soma(11, 12))
print()
print(comida_favorita('Churrasco'))  # Vai entrar na função de verificação
print(soma(11, 12))  # Vai entrar na função de verificação

"""

