"""
Windows: C:\\ = raiz
Posix (Linux e Mac-Os): / = raiz

- Sistemas posix são bem mais organizados e mais faceis de usar que Windows

PATH - Caminho do arquivo até o diretório
Comando 'PWD' - Mostra o caminho do path até o diretório corrente(o que se está no momento)

PATH ABSOLUTO - Mostra todo caminho do arquivo, da raiz até o arquivo
PATH RELATIVO - Mostra o caminho do path de forma abreviada... /home/workspace/backup/../

.. => Sobe(volta) um diretório da hierarquia
 . => Representa o diretório correte(local)

-   Para se manipular arquivos do sistema operacional, precisa do módulo 'OS' (operating system ou
sistema operacional)

EXEMPLOS

import os

corrente = os.getcwd()  # pega o diretório corrente(atual)
print(f'o PATH atual é {corrente}')

os.chdir("..")  # volta um diretório ou para o qual informar, se não informa nada, volta um apenas
corrente1 = os.getcwd()
print(f'o PATH atual é {corrente1}')

print(os.path.isabs('/home/paulo/../'))  # checa se o diretório é absoluto ou não

print(os.name)  # indica qual é o sistema operacional
print(os.sys.platform)  # indica qual é o sistema operacional

# Posix = Linux/mac
# nt / win32 = Windows

#  Mudar um deretório ou autocomplete do path
print(os.getcwd())
i = os.path.join(os.getcwd(), 'cursoPy')  # Junta o diretorio corrente com o diretório cursoPy e muda p/ o mesmo
os.chdir(i)
print(os.getcwd())

#  Função join concatena(junta), um path com outro
#  ESTUDAR MAIS SOBRE O MÉTODO JOIN

#  Lista os diretórios e arquivos

print(os.listdir())
print(len(os.listdir()))

# Listar com mais detalhes

scan = os.scandir()  # Gera um generator
print(scan)

arq = list(scan)
print(arq)
print(dir(arq[0]))
print(dir(arq[0].name))
arquivos.close()  # Scandir sempre deve ser fechado

import os
"""





