"""
São testes que coloca-se diretamente na DocString da função
 Para usar o doctest, no terminar deve ser chamado

 python3 -m doctest -v //nome_do_programa

"""

def soma(a, b):
    """Soma os numeros A e B
    
    >>> soma(1, 2)
    3
    """
    print(a + b)

soma(2, 2)
