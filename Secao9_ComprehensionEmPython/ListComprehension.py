"""
Com list comprehension, pode-se gerar novas listas com dados processados a partir de outro iterável.

SINTAXE
[dado for dado in iterável]

---------------------------------------------------------------------------------------------------------------------
numero = [1, 2, 3, 4]
#                    1º parte
res = [numero * 10 for numero in numero]  # TRADUÇÃO: Para cada numero dentro de numero, faça o numero x10
#      2º parte
print(res)

---------------------------------------------------------------------------------------------------------------------
#  EXEMPLO

numero = [1, 2, 3, 4]


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numero]
print(res)

---------------------------------------------------------------------------------------------------------------------
#  LIST COMPREHENSION vs LOOP

#                                        Loop

numeros = [1, 2, 3, 4]

numero_dobrado = []
for numero in numeros:
    num = numero * 2
    numero_dobrado.append(num)
print(numero_dobrado)


#                                        List Comprehension

print([numero * 2 for numero in numeros])
---------------------------------------------------------------------------------------------------------------------
#  OUTRO EXEMPLO
#  Separando todas as letras

nome = 'Paulo Fernando'
print([letra.upper() for letra in nome])

#  Pegando apenas a primeira letra de cada nome

amigos = ['Paulo', 'Gabriel', 'Habner']
print([amigo[0].title() for amigo in amigos])


#  Usando range

print([numero * 3 for numero in range(1, 10)])

---------------------------------------------------------------------------------------------------------------------
"""

#  Pode-se adicionar estruturas condicionais lógicas em List Comprehension

numeros = [1, 2, 3, 4]
pares = [numero for numero in numeros if numero % 2 == 0]
impar = [num for num in numeros if num % 2 != 0]
print(pares, impar)

res = [num * 2 if num % 2 == 0 else num / 2 for num in numeros]
print(res)









