"""
Try = Tente
Except = Excessão

try:
    //execução do bloco problemático

except:
    //o que fazer caso de erro no código

-------------------------------------------------------------------------------------------------------------------
#  EXEMPLO 1 - Forma não específica

try:
    geek()
except:
    print('Algo deu errado!')

#  O ideal é sempre tratar o erro de forma específica

#  FORMA 2 - Forma  ESPECÍFICA

try:
    geek()
except NameError:
    print('Função não existe!')

"""

#  EXEMPLO 3 - Forma ESPECÍFICA com detalhe de erro

try:
    geek()
except NameError as err:
    print(f'Você gerou o erro {err}')

#  Podem haver vários tratamentos de erro em um.
#  Por exemplo, vários except

