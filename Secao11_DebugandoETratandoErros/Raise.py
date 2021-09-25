"""
Serve para criar excessões e mensagens de erro

Modo de uso:  raise tipo_de_erro('Mensagem de erro')

"""

#  EXEMPLO


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O texto precisa ser string')
    if type(cor) is not str:
        raise TypeError('O texto precisa ser string')


#  OBS.:  O raise finaliza a função.
colore(1, 2)
