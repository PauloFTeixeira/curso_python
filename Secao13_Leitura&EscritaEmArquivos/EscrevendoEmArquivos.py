"""
OBS.:  Um arquivo aberto para leitura, somente pode ser lido
    Um arquivo aberto para escrita, somente pode ser escrito, sem poder ler

OBS.:  Ao abrir um arquivo no modo escrita "W", o mesmo é criado no sistema, caso não exista ainda.
    Para escrever após abrir o arquivo, usa-se a função write().
    Write recebe SEMPRE uma string como parâmetro

    Se um arquivo for aberto no modo "W" e contiver conteúdo nele, o mesmo é apagado e escrito do zero.

\n = quebra de linha


------------------------------------------------------------------------------------------------------------------
#  Exemplo

with open('novo.txt', 'w') as arq:
    arq.write('Primeiro lançamento \n')
    arq.write('Segundo lançamento \n')

with open('novo.txt') as arq:
    print(arq.read())

------------------------------------------------------------------------------------------------------------------
#  Exemplo mais Complexo

with open('fruteira.txt', 'w') as arq:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arq.write(fruta + '\n')
#            arq.write('\n')
        else:
            break

------------------------------------------------------------------------------------------------------------------
"""


