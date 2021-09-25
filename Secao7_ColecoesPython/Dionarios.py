"""
Dicionários (dict)
Em algumas linguagens, os dicionários Python são conhecidos como MAPAS.

Dicionários são coleções do tipo CHAVE/VALOR
São representados por {}

#  Exemplos

#  Forma 1 - Mais comum
paises = {'Br':'Brasil', 'EUA':'Estados Unidos', 'Py':'Paraguay'}
print(paises)
print(type(paises))
#  Chave e valor são separados por :  ch:vl
#  Tanto chave como valor podem ser de qualquer tipo de dado
#  Pode-se misturar tipos de dados

#  Forma 2 - Menos comum
pais = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(pais)
print(type(pais))

-------------------------------------------------------------------------------------------------------------------
#  ACESSO AOS ELEMENTOS
# Os elementos não são indexados
pais = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
paises = {'Br':'Brasil', 'EUA':'Estados Unidos', 'Py':'Paraguay'}

#    Forma 1 - via chave
print(pais['br'])
print(pais['eua'])
#  print(pais.['ru'])  #  Não existe, portanto se não usar o get, vai gerar um erro

#    Forma 2 - Acessando via get (recomendado)
print(pais.get('br'))
print(pais.get('eua'))
print(pais.get('ru'))  #  Não existe, neste caso, não gera um erro e sim um none.

# Exemplo
pais = pais.get('ru')
if pais:
    print(f'Encontrei {pais}')
else:
    print('Não encontrei')
# Sem o erro, pois None é falso, possibilitando continuar o código com um if.

#  Pode-se definir um valor padrão, para caso não haja o objeto procurado
pais = paises.get('Br', 'Não encontrei')
print(f'Encontrei o {pais}')

-------------------------------------------------------------------------------------------------------------------
#  VERIFICANDO SE UM OBJETO ESTÁ NO DICIONÁRIO

pais = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print('br' in pais)
print('ru' in pais)
print('Paraguay' in pais)
#  Obs.: Não busca valor, apenas chave

-------------------------------------------------------------------------------------------------------------------
# USAR QUALQUER TIPO DE DADO (INT, FLOAT, BOOLEAN), LISTA, TUPLA, DICIONÁRIO COMO CHAVE DE DICIONÁRIOS

localidade = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Paris',
    (37.7749, 122.4194): 'Escritório em Munique'
}
print(localidade)
#  OBS.: Tuplas são boas chaves para dicionários, pois são umutáveis

-------------------------------------------------------------------------------------------------------------------
#  ADICIONAR ELEMENTOS NO DICIONÁRIO

receita = {'jan': 100, 'fev': 200, 'mar': 300}

#  Forma 1 - Mais comum
receita['abr'] = 400
print(receita)

#  Forma 2 - Menos comun
novo = {'mai': 500}
receita.update(novo)
print(receita)
#  ou ainda
receita.update({'jun': 500})

-------------------------------------------------------------------------------------------------------------------
#  ATUALIZANDO DADOS EM UM DICIONÁRIO

receita = {'jan': 100, 'fev': 200, 'mar': 300}

#  Forma 1
receita['jan'] = 150
print(receita)

#  Forma 2
receita.update({'fev': 230})
print(receita)

#  Conclusão 1: adicionar ou atualizar dados é a mesma coisa;
#  Conclusão 2: Não pode ter chave repetida;

-------------------------------------------------------------------------------------------------------------------
#  REMOVENDO DADOS

receita = {'jan': 100, 'fev': 200, 'mar': 300}

#  Forma 1
receita.pop('mar')
print(receita)

#  OBS.: Obrigatório usar chave, senão encontrar o elemento, gera um erro.
#  OBS.: Ao remover um objeto, o valor é sempre retornado.

#  Forma 2
del receita['fev']
print(receita)
#  Se a chave não existir, gera um KeyError
#  Com del, não retorna o valor removido

-------------------------------------------------------------------------------------------------------------------
#  ONDE, COMO USAR?
#  Imagine um site de compras, onde se tem um carrinho de compras onde se adiciona os produtos.
#  ---------------------------------------------------------------------------
#  Poderia ser uma lista
carrinho = []
prod1 = ['Ração', 1, 50]
prod2 = ['oleo', 1, 200]
carrinho.append(prod1)
carrinho.append(prod2)
print(prod1, prod2)
#  neste caso, teriamos que saber o indice de cada produto
#  ---------------------------------------------------------------------------
#  Poderia ser uma tupla
produ1 = ['Ração', 1, 50]
produ2 = ['oleo', 1, 200]
carrinho.append(produ1)
carrinho.append(produ2)
print(produ1, produ1)

#  ---------------------------------------------------------------------------
#  Usando dicionario
carrinho1 = []
produto1 = {'nome':'Ração', 'qtd':1, 'valor':50}
produto2 = {'nome':'Oleo', 'qtd':1, 'valor':200}
carrinho1.append(produto1)
carrinho1.append(produto2)
print(carrinho1)
#  desta maneira, todos os elementos ficam mais fáceis de visualizar

--------------------------------------------------------------------------------------------------------------------
                                        #  METODOS DE DICIONÁRIO
--------------------------------------------------------------------------------------------------------------------
#  LIMPAR DICIONÁRIO
d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(d)

--------------------------------------------------------------------------------------------------------------------
#  COPIAR DICIONÁRIO PARA OUTRO
#  FORMA 1 - DEEP COPY (se mantem independente)
d = dict(a=1, b=2, c=3)
novo = d.copy()
print(d, novo)
novo['d'] = 4
print(d, novo)

# FORMA 2 - SHALLOW COPY (se mantem conectado)
novo1 = d
print(novo1, d)
novo1['d'] = 4
print(novo1, d)

--------------------------------------------------------------------------------------------------------------------
# FORMA NÃO USUAL DE CRIAR DICIONÁRIO

outro = {}.fromkeys('a', 'b')
print(outro)
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profissão'], 'desconhecido')
print(usuario)
#  O método fromkeys recebe dois parâmetros: um iterável e outro um valor
#  Ele gera uma chave para cada iterável
veja = {}.fromkeys('teste', 'valor')
print(veja)
#  Como neste exemplo, para cada letra dentro do iterável "teste", gera uma chave, que vai receber "valor" como valor
#  como não existe chave repetida em dicionário, os ultimos "t" e "e" são ignorados

veja1 = {}.fromkeys(range(1, 11), 'novo')
print(veja1)

--------------------------------------------------------------------------------------------------------------------
# COMO ITERAR SOBRE DICIONÁRIO
receita = {'jan': 100, 'fev': 200, 'mar': 300}
for chave in receita:
    print(chave)

for chave1 in receita:
    print(receita[chave1])

--------------------------------------------------------------------------------------------------------------------
#  ACESSO A TODAS AS CHAVES

receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

--------------------------------------------------------------------------------------------------------------------
#  ACESSANDO TODOS OS VALORES

receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita.values())

for valor in receita.values():
    print(valor)

--------------------------------------------------------------------------------------------------------------------
#  DESEMPACOTAMENTO DE DICIONÁRIO

receita = {'jan': 100, 'fev': 200, 'mar': 300}
for chave, valor in receita.items():
    print(f'Chave={chave}, valor={valor}')
#  ou ainda
print(receita.items())

--------------------------------------------------------------------------------------------------------------------
#  SOMA*, VALOR MÁXIMO*, VALOR MÍNIMO*, TAMANHO

receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))

"""

lista = [1, 2, 3]
a, b, v = lista
print(a, b, v)
