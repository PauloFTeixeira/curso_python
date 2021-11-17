"""
ATENÇÃO: Para ler ou escrever em arquivos no sistema, precisa-se de autorização

StringIO: Utilizadp para criar e ler arquivos em memória





#  Exemplo
from io import StringIO
mensagem = 'Apenas um texto de teste'

#  Pode ser um arquivo já com uma string ou vazio

arquivo = StringIO(mensagem)  #  é o mesmo que: arquivo = open('arquivos.txt', 'w')

#  Depois que o arquivo é criado, o restante é tudo igual.

arquivo.seek(0)
arquivo.write('Mais um teste')
arquivo.write('Novamente um teste')
print(arquivo.read())

arquivo.close()


"""


