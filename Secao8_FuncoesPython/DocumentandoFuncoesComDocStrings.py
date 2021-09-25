"""
Um comentário entre aspas tripla é uma DocString
"""

#  Exemplo de DocString


def diz_oi():
    """
    Está função vai trazer uma variável no retorno
    :return: Oi
    """
    return 'Oi!'


print(diz_oi())


def meu_nome(nome='Paulo', sobrenome='Teixeira'):
    """
    Função para cadastro de sobrenome
    :param nome: Digite seu nome
    :param sobrenome: Digite seu sobrenome
    :return: uma tupla com o nome e sobrenome
    """
    return nome, sobrenome


print(meu_nome())


#  Obs.:  Pode-se acessar a documentação de uma função usando a propriedade especial .__doc__
print(meu_nome.__doc__)
