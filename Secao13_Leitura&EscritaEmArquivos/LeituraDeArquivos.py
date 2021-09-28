"""
Para abrir o conteúdo de um arquivo em python, usa-se o OPEN()


opem() ->  Na forma mais simples, é passado um parâmetro, que é o nome do arquivo a ser lido

retorna um __io.textIOWrapper para ser trabalhado.

OBS.:  Por padrão, a função open() abre o arquivo somente para leitura. Este arquivo DEVE existir, ou então
gera FileNotFoundError

"""

#  Exemplo

#  Criar um file.txt
arquivo = open('file.txt')
print(arquivo)
print(type(arquivo))
#  mode 'r' -> leitura  #  r = read()#LER

#  Mostrar o conteúdo do arquivo
print(arquivo.read())
#  Se informa um parâmetro no read, limita a leitura até o índice informado.
#  O python usa um recurso chamado CURSOR, funcionando da mesma forma que em outros programas de texto

#  OBS.: A função read() lê todo o conteúdo do arquivo e retorna uma string.

arquivo.close()
