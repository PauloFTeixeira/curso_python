"""
Serve para filtrar dados de uma determinada função

-------------------------------------------------------------------------------------------------------------------
import statistics
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#  Calculo de estatístiva usando a função mean()
media = statistics.mean(dados)
print(media)


#  FUNÇÃO FILTER PRECISA DE DOIS PARÂMETROS <FUNÇÃO, ITERÁCEL>
filtro = filter(lambda valor: valor > media, dados)
print(list(filtro))
#  OBS.: Apaga os daos após serem usados

-------------------------------------------------------------------------------------------------------------------
paises = [' ', 'Brasil', ' ', ' ', 'Paraguai', ' ', 'Argentina']
res = filter(None, paises)
print(list(paises))


                            DIFERENÇA DE MAP E FILTER

Map revebe 2 parãmetros, e aplica a função a todos os dados do iterável

Filter recebe 2 parãmetros e filtra os iteráveis a partir do resultado da função

-------------------------------------------------------------------------------------------------------------------
usuarios = [
    {'username': 'Paulo', 'tweets': ['Eu adoro bolo']},
    {'username': 'Fernando', 'tweets': ['Eu adoro bolo', 'Gosto de andar de bike']},
    {'username': 'Lopes', 'tweets': ['Eu adoro bolo', 'Estudo python']},
    {'username': 'Teixeira', 'tweets': []}
]

#  Filtrar usuários inativos

#  FORMA 1
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)


#  FORMA 2
inativos2 = list(filter(lambda usuario: not usuario ['tweets'], usuarios))
print(inativos2)

-------------------------------------------------------------------------------------------------------------------
                                        COMBINAR FILTER COM MAP

nomes = ['Rivani', 'Duda', 'Paulinho']

#  Criar uma lista contendo sua instrutora e + nomes, desde que seja menor que 5 caracter.
#  A função abaixo filtra o nome que tem menos de 5 caractere.

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda  nome: len(nome) < 5, nomes)))
print(lista)


"""
