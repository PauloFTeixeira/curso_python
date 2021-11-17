"""

import os

#  Verificando se o arquivo existe ou não

print(os.path.exists("cursoPy"))  # Retorna True ou False
print(os.getcwd())

#  Criando arquivo localmente

# Exemplo1 - Forma não aconselhavel
open('arquivo.txt', 'w').close()


#  Exemplo2 - Forma aconselhável
with open('arquivo2.txt', 'w') as arq:
    pass  # = não faça nada 
import os


#  Criar arquivos - Únicos
os.mknod('/home/paulo/python/arq_teste.txt')

#  Criar diretórios - Únicos
os.mkdir('/home/paulo/python/teste')


#  Criando multiplos diretórios
os.makedirs('/home/paulo/paulo/teste/teste1', exist_ok=True)
#                                            Se existir, não gere erro


#  Renomear diretórios e Arquivos
os.rename('/home/paulo/python/algo', 'algo2')
#                     nome antigo     novo nome


#  Deletar arquivos
#  Não vai para a lixeira, deleta permanentemente
os.remove('/home/paulo/python/algo')
#                             Sempre último arquivo
#  No Windows, se o arquivo estiver aberto, gera erro
#  Se não existir o arquivo, gera erro


#  Deletar Diretório
os.rmdir('/home/paulo/python/algo')
#  Se tiver conteúdo, gera erro

OBS.: Para excluir tudo de um diretório, se usa um loop for
for arq in os.scandir('/home/paulo/python')
    if arquivo. is_file():
        os.remove(arquivo.path)


#  Remover arvore de diretório
os.removedirs('/home/paulo/python//teste/teste1')


#  Enviar arquivos para a lixeira

#  sudo apt install lsb-core
#  pip install send2trash

arq = '/home/paulo/python/teste'
arq.send2trash('teste')


#  Arquivos ou diretórios temporários

#  import os
#  import tempfile

with tempfile.TemporaryDirectory() as tmp:
    with open(os.path.join(tmp, 'arq.temp', 'w')) as arq:
        pass

#  Este tipo de arquivo só existe enquando o bloco With estiver aberto!


#  Para criar um arquivo temporário, em vez de with tempfile.TemporaryDirectory(), se usa
#  tempfile.TemporaryFile()
with tempfile.TemporaryFile() as tmp:
    tmp.white(b'texto de teste/n')
#             b = binário
#  Somente escrita de binário em qualquer arquivo temporário

with tempfile.NamedTemporaryFile() as tmp:
#             Nome aleatório ao arquivo    
    pass



"""








