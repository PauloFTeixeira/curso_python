"""
r -> abre para leitura  -  default
w -> abre para escrita (sobrescreve se já existir)
x -> abre para escrita, somente se ainda não existir
a -> abre para escrita, adicionando o conteúdo no final do arquivo, sem apagar o que já tinha
    OBS.:  No modo "A", se não existe ele cria, se existir ele escreve no final

+ -> abre no modo atualização, LEITURA e ESCRITA. Usado junto com outro modo
"""

with open('novo.txt', 'a+') as arq:
    arq.write('Atualização de teste \n')
    arq.write('Mais uma atualização de teste \n')

with open('novo.txt', 'r') as arq:
    print(arq.read())


