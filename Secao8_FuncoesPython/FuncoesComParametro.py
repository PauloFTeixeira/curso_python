"""
- Funções que recebem dados para serem processados dentro da mesma

Em um programa qualquer geralmente se tem:

Entrada->Processamento->Saída

Se for uma função, pode-se ter:
- Sem entrada
- Sem saída
- Com entrada mas sem saída
_ Sem entrada mas com saída
- Sem entrada e saída

-------------------------------------------------------------------------------------------------------------------
#  REFATORANDO UMA FUNÇÃO


def qudrado_de_sete():
    return 7*7


print(qudrado_de_sete())

                                    REFATORADO

def quadrado(numero):
    return numero * numero


print(quadrado(7))
print(quadrado(5))
print(quadrado(2))

ret = quadrado(8)
print(ret)

-------------------------------------------------------------------------------------------------------------------
#  REFATORANDO UMA FUNÇÃO

def cantar_parabens():
    print('Parabens para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!!')

                                    REFATORADO

def cantar(aniversariante):
    print('Parabens para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!!')

cantar_parabens()
cantar('Paulo')
-------------------------------------------------------------------------------------------------------------------
#  DEFINIÇÕES PODEM RECEBER UM OU MAIS PARÂMETRO


def soma(num1, num2):
    return num1 + num2


print(soma(2, 4))

-------------------------------------------------------------------------------------------------------------------
#  DIFERENÇA ENTRE PARÂMETRO E ARGUMENTO
- Parâmetro são variáveis declaradas na definição de uma função
- Argumentos são dados passados na execução de uma função
- A ordem dos argumentos importa, mesmo passado errado, vai ser exibida na ordem definida na função

-------------------------------------------------------------------------------------------------------------------
#  ARGUMENTOS NOMEADOS (KeyWord Arguments)
print(nome_completo(nome = nome, sobrenome = sobrenome))
ou
print(nome_completo)

"""










