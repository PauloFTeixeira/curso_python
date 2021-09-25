"""
!= -> Significa DIFERENTE

FORMA GERAL
while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.
Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.
num = 5
num < 10
"""
# EXEMPLO 1
numero = int(1)
while numero <10:
    print(numero)
    numero = numero+1
# OBS.: importante cuidar o critério de parada para não gerar um loop infinito.

# EXEMPLO 2 - loop infinito (sem um critério de parada)
# numero2 = int(1)
# while numero2 <10:
    # print(numero2)

# EXEMPLO 3
resposta = ' '
while resposta != 'Sim':
    resposta = input('Já terminou Jéssica? ')

