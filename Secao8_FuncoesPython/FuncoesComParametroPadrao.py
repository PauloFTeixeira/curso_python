"""
-Funções onde é opcional passar parâmetro

Ex.: print('Olá mundo')
Ex.: print()  # Não gera erro

---------------------------------------------------------------------------------------------------------------------
#  EXEMPLO DE FUNÇÃO COM PARÂMETRO OBRIGATÓRIO


def quadrado(numero):
    return numero ** 2


print(quadrado(2))

---------------------------------------------------------------------------------------------------------------------
#  EXEMPLO DE FUNÇÃO COM PARÂMETRO OPCIONAL

#                        opcional
def exponencial(numero, potencia = 2):
#                       se o valor não for passado fica o ja definido, senão é substituido pelo informado
    return numero ** potencia


print(exponencial(2, 5))
print(exponencial(5))  # Pelo padrão definido, eleva ao quadrado

OBS.: Os parâmetros com valores DEFAULT devem ser declarados sempre no final
---------------------------------------------------------------------------------------------------------------------
#  EXEMPLO COMPLEXO


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(nome='Paulo'))
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))  #  vai para o primeiro argumento - ORDEM IMPORTA
print(mostra_informacao('Ozzy'))
print(mostra_informacao(instrutor=False))

---------------------------------------------------------------------------------------------------------------------
#  PORQUE USAR PARÂMETROS COM VALOR DEFAULT
- Ser mais flexivel nas funções
- Evita erro com parâmetro incorreto
- Permite exemplos mais legíveis de código

Obs.: Pode-se usar qualquer tipo de dado como parâmetro default

---------------------------------------------------------------------------------------------------------------------
#  ATENÇÃO COM VARIÁVEL GLOBAL! (EVITAR O USO)

                             #  Exemplo 1: Maneira Errada
total = 0
def incremento():
    total = total + 1
    return total


print(incremento())

                             #  Exemplo 2: Maneira Correta
total = 0
def incremento():
    global total  # usar a palavra reservada 'global'
    total = total + 1
    return total


print(incremento())

#  Variável local de mesmo nome de uma global, a local tem preferẽncia na execução.

---------------------------------------------------------------------------------------------------------------------
#  PODE-SE DECLARAR FUNÇÃO DENTRO DE FUNÇÕES

def fora ():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())

#  A função nonlocal indica que é para ser usado a última variável da função anterior

---------------------------------------------------------------------------------------------------------------------
"""






