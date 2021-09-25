"""
Collections: High-performance container Datatypes
Tradução: Tipo de dados de container de alta performance

Counter: Recebe um iterável como parâmetro e cria um objeto do tipo "Collection Counter" que é parecido com um
dicionário, contendo como chave cada elemento da lista passado no parâmetro e como valor, a quantidade de ocorrencias
do elemento.


#  Exemplo 1

#  realizando o import
from collections import Counter
#  Pode-se usar qualquer iterável como parâmetro, por exemplo uma lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 8, 3, 6, 1, 1, 1, 1, 2, 5, 6, 6, 3, 3, 3, 5, 4, 4, 4, 4, 8, 7, 9, 4]
#  Utilizando o Counter
res = Counter(lista)
print(res)
print(type(res))


#  Exemplo 2

#  realizando o import
from collections import Counter
print(Counter('Paulo Fernando'))


#  Exemplo 3

#  realizando o import
from collections import Counter

texto = Meu Deus! Como é engraçado.
Eu nunca tinha reparado como é curioso um laço.
Uma fita dando voltas. Enrosca-se, mas não embola.
Vira, revira, circula e pronto, está dado o laço.
É assim que é o abraço (...)
Ah, então é assim o amor, a amizade, tudo que é sentimento.
Como um pedaço de fita.
Enrosca, segura um pouquinho, mas não pode se desfazer a qualquer hora, deixando livre as duas bandas do laço.
Por isso é que se diz: laço afetivo, laço de amizade.
E quando alguém briga então se diz: romperam-se os laços.
Então o amor, a amizade são isso.
Não prendem, não escravizam, não apertam, não sufocam.
Porque quando vira nó, já deixou de ser um laço.

palavras = texto.split()  #  Split separa todas as palavras
print(palavras)
res = Counter(palavras)  #  Vai contar quantas vezes cada palavra se repete
print(res)

#  Para encontrar as palavras que mais ocorrem no texto
print(res.most_common(5))
#                    x palavras que mais ocorrem no texto

"""



