"""

**kwargs

Desde que tenha (**), pode ser chamado de qualquer coisa.
**kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em dict.

-------------------------------------------------------------------------------------------------------------------
#  EXEMPLO


def cores(**kwargs):
    print(kwargs)


cores(Paulo='verde', Eduarda='azul')
for pessoa, cor in kwargs.items():
    print(f'A cor favorita de {pessoa} é {cor}')

OBS.: Os parâmetros *args e ** kwargs não são obrigatórios

-------------------------------------------------------------------------------------------------------------------
#  EXEMPLO COMPLEXO
def comprimento(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem é você'


print(comprimento())
print(comprimento(geek='Python'))
print(comprimento(geek='Oi'))
print(comprimento(geek='especial'))

-------------------------------------------------------------------------------------------------------------------
#  FUNÇÕES PODEM TER - (nesta ordem)

- Parâmetros obrigatórios
- *args
- Parâmetros default (não obrigatórios)
- **kwargs


def funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


funcao(8, 'Duda')
funcao(18, 'Eduarda', 4, 5, 6, Solteiro=True)
funcao(34, 'Paulo', eu='Não', voce='Vai')
funcao(19, 'Maria', 9, 4, 8, java=False, python=True)

-------------------------------------------------------------------------------------------------------------------
#  DESEMPACOTANDO **KWARGS

def nomes(**kwargs):
    return f"{kwargs['nome']}{kwargs['sobrenome']}"


nome = {'nome': 'Paulo', 'sobrenome': ' Teixeira'}


print(nomes(**nome))


Os nomes das chaves dos dict's devem ser as mesmas dos parâmetros das funções

-------------------------------------------------------------------------------------------------------------------
"""