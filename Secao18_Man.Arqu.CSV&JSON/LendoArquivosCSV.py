"""
CSV - Comma Separeted Values - Valores separados por vírgula
Pode ter outros separadores(, . ; " "), o importante é o padrão

Dados CSV para estudo
https://dados.gov.br/dataset


#  Para fazer a leitura de arquivo .csv

with open('lutadores.csv') as arq:  # Não é a forma ideal
    dados = arq.read()
    print(type(dados))
    print(dados)


Em Python possui duas formas diferentes de ler arquivos CSV
    - reader => Permite iterar sobre as linhas do arquivo CSV como lista
    - DicReader => Permite iterar sobre as linhas do arquivo CSV como OrderedDict


#  USANDO READER
from csv import reader, DictReader

with open('lutadores.csv') as arq:
    #  Por padrão, o separador é ',', para mudar, sua o delimiter
    leitor_csv = reader(arq, delimiter=',')  # Deliomiter é usado para mudar o delimitador
    next(leitor_csv)  # Pula a primeira linha. Leitor_csv é um iterator, pode usar next
    for lin in leitor_csv:
        print(f'{lin[0]} nasceu no(a) {lin[1]} mede {lin[2]} centímetros')
#  Cada linha do arquivo, gerar uma lista

#  USANDO DICTREADER

with open('lutadores.csv') as arq:
    #  Por padrão, o separador é ',', para mudar, sua o delimiter
    leitor = DictReader(arq, delimiter=',')  # Deliomiter é usado para mudar o delimitador
    #  Cada linha é um orderedDict, o cabçalho se torna a chave, o resto valor
    for lin in leitor:
        print(f"{lin['Nome']} nasceu no(a) {lin['País']} e mede {lin['Altura (em cm)']}")

"""


