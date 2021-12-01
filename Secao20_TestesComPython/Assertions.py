"""
Assertions (Afirmações/Checagem/Questionamentos)

Utiliza-se a palavras 'assert' para realizar simples afirmações nos testes
    Utilizada para verificar se uma expressão é valida ou não
    Se Valida = retorna None
    Se Inválida = retorna AssertionError

    Pode-se especificar, opcionalmente, um segundo argumento ou uma mensagem de erro



def soma_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos precisam ser positivos'  # Se os dois não forem positivos
    #  vai avisar que ambos precisam ser positivos
    return a + b

print(soma_positivos(2, 4))
print(soma_positivos(2, -3))

ALERTA: Se o programa for rodado com o parâmetro -O, o assertion não funciona



def comer(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'churrasco',
        'cachorro quente',
    ], 'A comida precisa ser fest-food'
    return f'Estou comendo {comida}'

print(comer('churrasco'))
print(comer('batata frita'))


"""



