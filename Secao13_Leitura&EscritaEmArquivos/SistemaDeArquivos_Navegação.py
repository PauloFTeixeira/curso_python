"""
Windows: c:\\
Posix: /

Path: caminho do arquivo até o diretório

comando pwd -> mostra o caminho do Path

Path absoluto: Todo o caminho, da raiz até o arquivo
Path relativo: Ex. /home/workspace/backup/../
.. -> volta um diretório na hierarquia
. -> deretório local

Para manipular arquivos do sistema operacional, precisa do módulo 'OS'
    OS = Operating System -> Sistema Operacional


import os

-- getcwd: pega o diretório de trabalho corrente. Path absoluto
-- chdir: Volta para um diretório específico ou ".." para voltar um na linha hierárquica

--    Para checar se um diretório é absoluto ou relativo:
print(os.isabs('/home/paulo'))

-- Identificar qual o sistema operacional
print(os.name)


"""
import os
print(os.name)
