"""
Metadatas: São dados intrínsecos em arquivos. São todas as informações de um arquivo

Wraps: São funções que envolvem elementos com diversas finalidades


from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        '''Sou uma função dentro de outra'''
        print(f'Voce está chamando a função {funcao.__name__}')
        print(f'Aqui está sua documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    '''Soma dois números'''
    return a + b

print(soma(10, 20))
print(soma.__name__)  
print(soma.__doc__)
# Sem o whaps, a informaçaõ de nome e documentação seria perdida, pois retornaria nome e 
# documentação da função decoradora

"""
