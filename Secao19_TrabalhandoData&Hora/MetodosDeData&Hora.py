"""

#  Com now() pode-se especificar um timezone (fuso horário)
agora = datetime.datetime.now()  # Now() == agora
hoje = datetime.datetime.today()  # Today == hoje



#  MUDANÇAS OCORRENDO A MEIA NOITE

# Serve, por exemplo, para programar uma data e uma hora
#  datetime.time() => esse parametro vazio, faz o horário ficar zerado
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), 
datetime.time())
print(manutencao)

#  ENCONTRAR O DIA DA SEMANA - WEEKDAY
#  0 - Segunda
#  1 - Terça
#  2 - Quarta
#  3 - Quinta
#  4 - Sexta
#  5 - Sábado
#  6 - Domingo
print(manutencao.weekday())




#  Formatando Datas e Horas - Stringftime - String Format Time
hoje = datetime.datetime.today()
print(hoje)
hoje_formatado = hoje.strftime('%d/%m/%Y')  # Y = Ano com 4 digito.  y = ano com 2 digitos
print(hoje_formatado)


import datetime
from textblob import Textblob
#  Traduzindo do ingles para o Português e formatando a Data
def formata_data (data):
    return f"{data.day} de {Textblob(data.strftime('%B')).translate(to='pt-nr')} de {data.year}"


hoje = datetime.datetime.today()
print(formata_data(hoje))



#  Transformando String em Datetime

nascimento = input('Informe sua data de nascimento dd/mm/aaaa: ')
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

"""

import timeit, functools

#  Marcando tempo de Execução - timeit

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000))
#  Partial - qual função a ser testada
#  2 - paramentro de entrada da função
#  number - Quantas vezes vai executar a função


#  NESTA FUNÇÃO, CALCULAMOS O TEMPO DE EXECUÇÃO DA FUNÇÃO 10 MIL VEZES




